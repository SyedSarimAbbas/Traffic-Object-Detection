---
title: Traffic Detection
emoji: 🚗
colorFrom: yellow
colorTo: red
sdk: docker
app_file: app.py
pinned: false
---

# 🚗 YOLO Vehicle Detection App

This is a Flask web application that uses a YOLO model (`Vehicals_Detection_Model.pt`) to detect vehicles in uploaded images.

---

## Traffic Detection with YOLO + Flask

This project is a **web application** built with **Flask** and **YOLOv8** that allows users to upload images and detect vehicles in them.  
It provides an easy-to-use interface where predictions are displayed directly on the uploaded image.

---

##  Features
- Upload an image and get **vehicle detections** using a trained YOLO model.  
- Results are shown with **bounding boxes** directly on the image.  
- Clean **HTML/CSS UI**.  
- Flask-powered web app, ready for **deployment on Hugging Face Spaces**.  

---

## 🛠 Tech Stack
- **Python 3.10+**
- **Flask**
- **Ultralytics YOLOv8**
- **HTML / CSS (Jinja2 templates)**

---

##  Project Structure
Traffic Detection Project/
│── app.py # Flask app
│── requirements.txt # Python dependencies
│── Vehicals_Detection_Model.pt # YOLO model
│── static/ # Static assets (background, results, CSS)
│ ├── background_cover/bgcover.jpeg
│ └── results/
│── templates/ # HTML templates
│ ├── index.html
│ ├── predict.html
│ └── result.html

yaml
Copy code

---

##  Installation (Local)

1. **Clone the repository**
   ```bash
   git clone https://github.com/SyedSarimAbbas/Traffic-Object-Detection.git
   cd Traffic-Object-Detection
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the Flask app

bash
Copy code
python app.py
Open in browser

cpp
Copy code
http://127.0.0.1:7860

# Deployment on Hugging Face Spaces
Create a new Space (SDK: docker).

Push your project files:

app.py

Vehicals_Detection_Model.pt

requirements.txt

Dockerfile

templates/

static/

README.md