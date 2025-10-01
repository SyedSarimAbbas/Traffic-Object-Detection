from flask import Flask, render_template, request, send_file
import os
from ultralytics import YOLO
import json

# Load YOLO model
model = YOLO("Vehicals_Detection_Model.pt")

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
JSON_FOLDER = 'json_results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
os.makedirs(JSON_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No file selected", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Run YOLO detection
    results = model.predict(
        source=filepath,
        save=True,
        project=RESULTS_FOLDER,
        name="output",
        exist_ok=True
    )

    # Extracting prediction results
from flask import Flask, render_template, request, redirect, url_for
import os
from ultralytics import YOLO
import json
import uuid

# Load YOLO model
model = YOLO("Vehicals_Detection_Model.pt")

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'static/results'
JSON_FOLDER = 'json_results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
os.makedirs(JSON_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_page')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No file selected", 400

    # Generate unique filename to avoid overwrites
    unique_name = str(uuid.uuid4()) + "_" + file.filename
    filepath = os.path.join(UPLOAD_FOLDER, unique_name)
    file.save(filepath)

    # Run YOLO detection
    results = model.predict(
        source=filepath,
        save=True,
        project=RESULTS_FOLDER,
        name="output",
        exist_ok=True
    )

    # Extract predictions and save JSON
    predictions = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        confidence = float(box.conf[0])
        xyxy = box.xyxy[0].tolist()
        class_name = model.names[cls_id]

        predictions.append({
            "class_id": cls_id,
            "class_name": class_name,
            "confidence": confidence,
            "bbox": xyxy
        })

    json_filename = os.path.splitext(unique_name)[0] + ".json"
    json_path = os.path.join(JSON_FOLDER, json_filename)

    with open(json_path, "w") as f:
        json.dump(predictions, f, indent=4)

    # Get result image path (YOLO saves it in results/output)
    result_image_path = os.path.join(results[0].save_dir, unique_name)

    # Move result image to static/results for serving
    final_path = os.path.join(RESULTS_FOLDER, unique_name)
    if os.path.exists(result_image_path):
        os.rename(result_image_path, final_path)

    # Redirect to result page
    return redirect(url_for("result_page", filename=unique_name))

@app.route('/result/<filename>')
def result_page(filename):
    return render_template('result.html', result_image="results/" + filename)

if __name__ == '__main__':
    app.run(debug=True)
