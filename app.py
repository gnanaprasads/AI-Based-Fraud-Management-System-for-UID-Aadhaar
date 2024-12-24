from flask import Flask, request, render_template, jsonify
import os
from zipfile import ZipFile
from easyocr import Reader
from ultralytics import YOLO

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['TEMP_FOLDER'] = 'temp/'

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['TEMP_FOLDER'], exist_ok=True)

# Initialize OCR reader and models
reader = Reader(['en'])
classifier = YOLO("models/classification_model.pt")
detector = YOLO("models/detection_model.pt")

def process_image(image_path):
    """Extract text from the Aadhaar image."""
    text_data = reader.readtext(image_path)
    return {line[1]: line[2] for line in text_data}

def classify_image(image_path):
    """Classify an image to verify Aadhaar authenticity."""
    result = classifier.predict(image_path)
    return result

def detect_fields(image_path):
    """Detect fields like name, DOB, etc., in Aadhaar image."""
    result = detector.predict(image_path)
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'zipfile' in request.files and 'excelfile' in request.files:
        zip_file = request.files['zipfile']
        excel_file = request.files['excelfile']

        # Save uploaded files
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_file.filename)
        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_file.filename)
        zip_file.save(zip_path)
        excel_file.save(excel_path)

        return jsonify({"message": "Files uploaded successfully!"})
    return jsonify({"error": "Both files are required."}), 400

@app.route('/process', methods=['GET'])
def process_files():
    # Locate uploaded files
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    zip_files = [f for f in uploaded_files if f.endswith('.zip')]
    excel_files = [f for f in uploaded_files if f.endswith('.xlsx')]

    if not zip_files or not excel_files:
        return jsonify({"error": "Required files are missing."}), 400

    zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_files[0])
    excel_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_files[0])

    # Extract ZIP files
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(app.config['TEMP_FOLDER'])

    extracted_data = []
    for image_file in os.listdir(app.config['TEMP_FOLDER']):
        image_path = os.path.join(app.config['TEMP_FOLDER'], image_file)
        
        # Process image
        text_data = process_image(image_path)
        classification_result = classify_image(image_path)
        detection_result = detect_fields(image_path)

        extracted_data.append({
            "image": image_file,
            "text_data": text_data,
            "classification": classification_result,
            "detections": detection_result
        })

    return jsonify({"message": "Processing completed!", "data": extracted_data})

if __name__ == '__main__':
    app.run(debug=True)
