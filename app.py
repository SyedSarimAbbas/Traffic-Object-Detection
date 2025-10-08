from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
import os
import json
import uuid
import shutil

# Initialize Flask with explicit template and static folders
app = Flask(__name__, template_folder='templates', static_folder='static')

# Print debug information at startup
print("=" * 50)
print("Flask App Configuration:")
print(f"Root Path: {app.root_path}")
print(f"Template Folder: {app.template_folder}")
print(f"Static Folder: {app.static_folder}")
print(f"Current Working Directory: {os.getcwd()}")

# Check if templates exist
template_path = os.path.join(app.root_path, 'templates')
if os.path.exists(template_path):
    print(f"✅ Templates directory found: {template_path}")
    print(f"   Files: {os.listdir(template_path)}")
else:
    print(f"❌ Templates directory NOT found: {template_path}")

# Check if static exists
static_path = os.path.join(app.root_path, 'static')
if os.path.exists(static_path):
    print(f"✅ Static directory found: {static_path}")
    print(f"   Files: {os.listdir(static_path)}")
else:
    print(f"❌ Static directory NOT found: {static_path}")
print("=" * 50)

# Folder paths
UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'static/results'
JSON_FOLDER = 'json_results'

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
os.makedirs(JSON_FOLDER, exist_ok=True)

# Lazy model loading (prevents timeout on startup)
model = None
def get_model():
    global model
    if model is None:
        model_path = "Vehicals_Detection_Model.pt"
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        model = YOLO(model_path)
    return model


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/predict_page')
def predict_page():
    """Prediction upload page"""
    return render_template('predict.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle image upload and run YOLO detection"""
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No file selected", 400

    # Validate file extension
    allowed_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in allowed_extensions:
        return "Invalid file type. Please upload an image.", 400

    # Generate unique filename
    unique_name = str(uuid.uuid4()) + "_" + file.filename
    filepath = os.path.join(UPLOAD_FOLDER, unique_name)
    file.save(filepath)

    try:
        # Load YOLO model
        yolo_model = get_model()

        # Run detection
        results = yolo_model.predict(
            source=filepath,
            save=True,
            project=RESULTS_FOLDER,
            name="output",
            exist_ok=True,
            verbose=False
        )

        # Extract predictions
        predictions = []
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            xyxy = box.xyxy[0].tolist()
            class_name = yolo_model.names[cls_id]
            predictions.append({
                "class_id": cls_id,
                "class_name": class_name,
                "confidence": confidence,
                "bbox": xyxy
            })

        # Save JSON
        json_filename = os.path.splitext(unique_name)[0] + ".json"
        json_path = os.path.join(JSON_FOLDER, json_filename)
        with open(json_path, "w") as f:
            json.dump(predictions, f, indent=4)

        # Get YOLO result image
        result_image_path = os.path.join(results[0].save_dir, os.path.basename(filepath))
        final_path = os.path.join(RESULTS_FOLDER, unique_name)

        # Move result image safely
        if os.path.exists(result_image_path):
            shutil.move(result_image_path, final_path)
        else:
            # Fallback: copy original if detection image not found
            shutil.copy(filepath, final_path)

        # Clean up uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)

        # Redirect to results page
        return redirect(url_for("result_page", filename=unique_name))

    except Exception as e:
        # Clean up on error
        if os.path.exists(filepath):
            os.remove(filepath)
        return f"Prediction error: {str(e)}", 500


@app.route('/result/<filename>')
def result_page(filename):
    """Show result page with detected image"""
    result_path = os.path.join(RESULTS_FOLDER, filename)
    if not os.path.exists(result_path):
        return "Result image not found", 404
    return render_template('result.html', result_image="results/" + filename)


@app.route('/health')
def health():
    """Health check endpoint for deployment platforms"""
    return {"status": "healthy"}, 200


if __name__ == '__main__':
    # Hugging Face Spaces listens on port 7860
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port, debug=False)