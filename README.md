# Aadhaar Fraud Management System

## Overview

This project integrates a classification model, a detection model, and OCR into a unified AI-based Aadhaar Fraud Management System. It processes user documents and compares extracted data with existing records to detect potential fraud. The application includes a Flask-based backend and a user-friendly interface to ensure smooth functionality.

## Features

1. **Data Input**:
   - Upload a ZIP folder containing multiple user documents (images).
   - Upload an Excel file with existing user records (name, UID, address).
2. **AI Models**:
   - **Classification Model**: Identifies if a document is an Aadhaar card.
   - **Detection Model**: Detects and crops relevant sections (name, UID, address) from Aadhaar cards.
   - **OCR Model**: Extracts text from cropped sections.
3. **Data Comparison**:
   - Compares extracted data with records in the Excel file.
   - Generates match percentages based on business rules.
4. **Output**:
   - Provides a detailed report with match scores for each user.
5. **Web Interface**:
   - Allows users to upload files, process data, and view results seamlessly.

## Application Workflow

1. **Input Data**:
   - Users upload a ZIP file and an Excel file.
2. **Classification**:
   - Determine if the document is an Aadhaar card.
3. **Detection**:
   - Detect and crop fields (name, UID, address) from Aadhaar cards.
4. **OCR**:
   - Extract text from the cropped fields.
5. **Comparison**:
   - Compare extracted data with Excel records.
   - Calculate match scores based on predefined business rules.
6. **Output**:
   - Generate a report with the match scores.

## Project Structure

```
project/
|-- app.py
|-- models/
|-- static/
|-- templates/
|-- uploads/
|-- requirements.txt
```

## Backend Architecture

The backend is built using Flask to handle logic and provide APIs for communication with the frontend.

### API Endpoints

1. `/upload`: Handle ZIP and Excel file uploads.
2. `/process`: Process files through the AI models.
3. `/results`: Return the match scores.

## Frontend Design

The user interface allows seamless interaction with the application, including file uploads, processing, and result visualization.

### Features

1. **Upload Section**: Fields to upload ZIP and Excel files.
2. **Process Button**: Triggers the backend pipeline.
3. **Results Display**: Displays match scores in a table.

## Model Integration

The classification, detection, and OCR models are combined into a processing pipeline within Flask.

### Integration Steps

1. Load the models at the start of the application.
2. Create functions to handle classification, detection, and OCR processes.
3. Implement a pipeline to process each file and extract the necessary data.

## Database and Scoring

- Use SQLite or PostgreSQL to store extracted data and results.
- Implement scoring logic to compare extracted data with existing records.

### Scoring Logic

1. Calculate match percentages based on predefined business rules.
2. Store results in the database for easy retrieval.

## Next Steps

1. Implement the Flask backend and UI as outlined.
2. Code and test the business rules for scoring.
3. Test the integrated application with sample data.
4. Deploy the application using a server (e.g., AWS, Heroku).

## Installation

1. Clone the repository:
   
   git clone https://gnanaprasads/AI-Based-Fraud-Management-System-for-UID-Aadhaar.git
   cd aadhaar-fraud-management
   
2. Install dependencies:
   
   pip install -r requirements.txt
  
3. Run the application:
   
   python app.py
   
4. Access the app at `http://127.0.0.1:5000`.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or bugs.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

