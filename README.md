<<<<<<< HEAD
---
title: Traffic Detection
emoji: 🚗
colorFrom: yellow
colorTo: red
sdk: docker
app_file: app.py
pinned: false
---

#  YOLO Vehicle Detection App

This is a Flask web application that uses a YOLO model (`Vehicals_Detection_Model.pt`) to detect vehicles in uploaded images.

---

##  Traffic Detection with YOLO + Flask
=======
#  Traffic Detection with YOLO + Flask
>>>>>>> f7e97ac9529e03507366d40114f7c42879efd53e

This project is a **web application** built with **Flask** and **YOLOv8** that allows users to upload images and detect vehicles in them.  
It provides an easy-to-use interface where predictions are displayed directly on the uploaded image.

---

##  Features
<<<<<<< HEAD
- Upload an image and get **vehicle detections** using a trained YOLO model  
- Results are shown with **bounding boxes** directly on the image  
- Clean **HTML/CSS UI**  
- Flask-powered web app, ready for **deployment on Hugging Face Spaces**
=======
- Upload an image and get **vehicle detections** using a trained YOLO model.  
- Results are shown with **bounding boxes** directly on the image.  
- Clean **HTML/CSS UI** with background customization.  
- Flask-powered web app, ready for **deployment on Hugging Face Spaces**.  
>>>>>>> f7e97ac9529e03507366d40114f7c42879efd53e

---

##  Tech Stack
- **Python 3.10+**
- **Flask**
- **Ultralytics YOLOv8**
- **HTML / CSS (Jinja2 templates)**

---

##  Project Structure
<<<<<<< HEAD

=======
>>>>>>> f7e97ac9529e03507366d40114f7c42879efd53e
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
<<<<<<< HEAD
   cd Traffic-Object-Detection
Install dependencies
=======
   cd traffic-detection
##Install dependencies:
>>>>>>> f7e97ac9529e03507366d40114f7c42879efd53e

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
  Deployment on Hugging Face Spaces
Create a new Space on Hugging Face

<<<<<<< HEAD
SDK: Docker
=======
## 🌐 Deployment on Hugging Face Spaces
Create a new Space (SDK: Flask).
>>>>>>> f7e97ac9529e03507366d40114f7c42879efd53e

Space type: Static or Flask

Push your project files to the Space:

app.py

Vehicals_Detection_Model.pt

requirements.txt

Dockerfile

templates/

static/

README.md

Hugging Face will automatically build and launch your app using the Dockerfile.

Make sure your Flask app runs on port 7860:

python
Copy code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
<<<<<<< HEAD
    
# License
This project is licensed under the MIT License.
=======

📜 License
This project is licensed under the MIT License.
>>>>>>> f7e97ac9529e03507366d40114f7c42879efd53e
