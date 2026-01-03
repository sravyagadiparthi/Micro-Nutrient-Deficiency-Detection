# Micro Nutrient Deficiency Detection

This project detects micronutrient deficiencies in banana plants using image processing and machine learning.

## Project Overview
Banana Deficiency Detection is a web-based application that allows users to upload images of banana leaves and identifies possible micronutrient deficiencies using a trained machine learning model. The application uses a Flask backend to serve the predictions and a web interface for easy interaction.

## Features
- Upload banana leaf images
- Detect micronutrient deficiencies
- Web-based user interface
- Real-time predictions using a trained ML model

## Technologies Used
- Python
- Flask
- TensorFlow / Keras
- OpenCV
- HTML, CSS, JavaScript
- NumPy, Pandas

## How to Run (Step by Step)

Follow these steps to run the Banana Deficiency Detection project locally:

step 1. **Clone the repository**  
```bash
git clone https://github.com/your-username/Micro-Nutrient-Deficiency-Detection.git
Navigate to the project folder

step 2.cd Banana_deficiency_app
Create a virtual environment

step 3.python -m venv venv
Activate the virtual environment

step 4.
Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate
Install required dependencies

step 5.pip install -r requirements.txt
Run the Flask backend

step 6.python app.py
The backend will start at http://127.0.0.1:5000/

Open the web interface

Open http://127.0.0.1:5000/ in your browser

Use the app

Upload a banana leaf image

The app will detect possible micronutrient deficiencies
