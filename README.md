#  Traffic Detection with YOLO + Flask

This project is a **web application** built with **Flask** and **YOLOv8** that allows users to upload images and detect vehicles in them.  
It provides an easy-to-use interface where predictions are displayed directly on the uploaded image.

---

##  Features
- Upload an image and get **vehicle detections** using a trained YOLO model.  
- Results are shown with **bounding boxes** directly on the image.  
- Clean **HTML/CSS UI** with background customization.  
- Flask-powered web app, ready for **deployment on Hugging Face Spaces**.  

---

##  Tech Stack
- **Python 3.10+**
- **Flask**
- **Ultralytics YOLOv11**
- **HTML / CSS (Jinja2 templates)**

---

##  Project Structure
Traffic Detection Project/
│── app.py # Flask app
│── requirements.txt # Python dependencies
│── Vehicals_Detection_Model.pt # YOLO model
│── static/ # Static assets (background, results, CSS)
│ ├── background_cover/bgcover.jpeg
│ ├── results/
│── templates/ # HTML templates
│ ├── home.html
│ ├── predict.html
│ ├── result.html
|Vehicals_Detection_Model.pt

yaml
Copy code

---

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SyedSarimAbbas/Traffic-Object-Detection.git
   cd traffic-detection
##Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
Open in browser:

cpp
Copy code
http://127.0.0.1:5000

## 🌐 Deployment on Hugging Face Spaces
Create a new Space (SDK: Flask).

Push this repo to your Hugging Face Space.

Make sure to set the app port in app.py:

python
Copy code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)

📜 License
This project is licensed under the MIT License.
