
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import base64
from PIL import Image
from io import BytesIO
from recommendation_engine import RecommendationEngine

app = Flask(__name__)
model = load_model('model/banana_deficiency_model.h5')
classes = ['Boron', 'Calcium', 'Iron', 'Potassium', 'Magnesium', 'Manganese', 'Sulphur', 'Zinc', 'Healthy']
recommendation_engine = RecommendationEngine()

def predict_deficiency(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    return classes[np.argmax(prediction)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route('/webcam')
def webcam_page():
    return render_template('webcam.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['leaf_image']
    filepath = os.path.join('static', file.filename)
    file.save(filepath)
    result = predict_deficiency(filepath)
    recommendation = recommendation_engine.get_recommendation(result)
    return render_template('result.html',
                           prediction=result,
                           image_path=filepath,
                           recommendation=recommendation)

@app.route('/predict_webcam', methods=['POST'])
def predict_webcam():
    data_url = request.form['image_data']
    header, encoded = data_url.split(",", 1)
    image_data = base64.b64decode(encoded)
    img = Image.open(BytesIO(image_data)).convert('RGB').resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    result = classes[np.argmax(prediction)]
    recommendation = recommendation_engine.get_recommendation(result)
    img.save(os.path.join('static', 'webcam_capture.png'))
    return render_template('result.html',
                           prediction=result,
                           image_path='static/webcam_capture.png',
                           recommendation=recommendation)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form['feedback']
    with open('feedback_log.txt', 'a') as f:
        f.write(f"{feedback}\n")
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
