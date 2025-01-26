from flask import Flask, request, jsonify, render_template, send_file
import os
from ultralytics import YOLO
from easyocr import Reader
import zipfile
import pandas as pd
import cv2
from fuzzywuzzy import fuzz, process
import re
import numpy as np
import json
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'zip', 'xlsx'}
app.config['RESULTS_FOLDER'] = 'results/'
app.config['DATABASE'] = 'results_ack.db'

classifier = YOLO("./models/classification.pt")
detector = YOLO("./models/detection.pt")
reader = Reader(['en'])

def process_image(image_path):
    if classifier.predict(image_path)[0].probs.numpy().top1 == 0:
        fields = detector(image_path)
        image = cv2.imread(image_path)
        extracted_data = {}
        for field in fields[0].boxes.data.tolist():
            x1, y1, x2, y2, confidence, class_id = map(int, field[:6])
            field_class = detector.names[class_id]
            cropped_roi = image[y1:y2, x1:x2]
            gray_roi = cv2.cvtColor(cropped_roi, cv2.COLOR_BGR2GRAY)
            text = reader.readtext(gray_roi, detail=0)
            extracted_data[field_class] = ' '.join(text)
        return extracted_data
    return None

# Helper Functions
def normalize_text(text):
    if not text:
        return "text empty"
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join(text.split()).lower()

def calculate_match_score(input_value, extracted_value):
    if pd.isna(input_value) or pd.isna(extracted_value):
        return 0
    return fuzz.ratio(str(input_value), str(extracted_value))

def name_match(input_name, extracted_name):
    if extracted_name is None:
        return False
    input_name = normalize_text(input_name)
    extracted_name = normalize_text(extracted_name)

    if input_name == extracted_name:
        return True

    input_parts = input_name.split()
    extracted_parts = extracted_name.split()

    if sorted(input_parts) == sorted(extracted_parts):
        return True

    if len(input_parts) == 2 and len(extracted_parts) == 3:
        if input_parts[0] == extracted_parts[0] and input_parts[1] == extracted_parts[2]:
            return True
    if len(input_parts) == 3 and len(extracted_parts) == 2:
        if extracted_parts[0] == input_parts[0] and extracted_parts[1] == input_parts[2]:
            return True

    for part in input_parts:
        if part not in extracted_parts:
            return False
    return True

def address_match(input_address, extracted_address):
    print(input_address, extracted_address)
    if input_address is None or extracted_address is None:
        return False, 0.0, {}

    # Handle input_address if it's a Series
    if isinstance(input_address, pd.Series):
        input_address = input_address.to_dict()
    
    print(extracted_address)
    extracted_address = normalize_text(extracted_address)
    final_score = 0
    print(extracted_address)
    weights = {
        "State": 0.2,
        "Landmark": 0.2,
        "Premise Building Name": 0.2,
        "City":0.2,
        "Street Road Name":0.1,
        "Floor Number": 0.05,
        "House Flat Number": 0.05
    }
    tokens = extracted_address.split(" ")
    # Component matching logic
    for field, weight in weights.items():
        input_value = input_address.get(field, "")
        match_score = fuzz.token_set_ratio(normalize_text(input_value), extracted_address) if input_value else 0
        input_address[field + " Match Score"] = match_score
        final_score += match_score * weight
    pincode_score = process.extractOne(input_address.get("PINCODE"), tokens)[1]
    input_address['PINCODE Match Score'] = pincode_score
    pincode_matched = True if input_address['PINCODE Match Score'] == 100 else False

    return final_score >= 70 and pincode_matched, final_score, input_address

def compare_data(input_data, json_data):
    excel_data = input_data.copy()
    for idx, row in excel_data.iterrows():
        serial_no = row.get("SrNo")
        uid = row.get("UID")
        extracted = json_data.get(serial_no)

        if extracted:
            extracted_uid = extracted.get("uid", "").replace(" ", "")
            extracted_name = extracted.get("name", "")
            extracted_address = extracted.get("address", "")
            row['Extracted UID'] = extracted_uid
            row['Extracted Name'] = extracted_name
            row['Extracted Address'] = extracted_address
            # UID Match
            uid_match = uid == extracted_uid
            uid_score = 100 if uid_match else 0
            row['UID Match Score'] = uid_score

            # Name Match
            name_match_result = name_match(row.get("Name"), extracted_name)
            name_score = calculate_match_score(row.get("Name"), extracted_name)
            row['Name Match Score'] = name_score
            row['Name Match Percentage'] = name_score

            # Address Match
            address_match_result, address_score, partial_scores = address_match(row, extracted_address)
            if partial_scores:
                row['House Flat Number Match Score'] = partial_scores['House Flat Number Match Score']
                row['Street Road Name Match Score'] = partial_scores['Street Road Name Match Score']
                row['City Match Score'] = partial_scores['City Match Score']
                row['Floor Number Match Score'] = partial_scores['Floor Number Match Score']
                row['Premise Building Name Match Score'] = partial_scores['Premise Building Name Match Score']
                row['Landmark Match Score'] = partial_scores['Landmark Match Score']
                row['State Match Score'] = partial_scores['State Match Score']
                row['Final Address Match'] = address_match_result
                row['Final Address Match Score'] = address_score
                row['PINCODE Match Score'] = partial_scores['PINCODE Match Score']
            
            # Final Match
            overall_match = uid_match and name_match_result and address_match_result

            row['Overall Match'] = overall_match

            if overall_match:
                row['Final Remarks'] = "All matched"
            elif not uid_match:
                row['Final Remarks'] = "UID mismatch"
            elif not name_match_result:
                row['Final Remarks'] = "Name mismatch"
            elif not address_match_result:
                row['Final Remarks'] = "Address mismatch"
            else:
                if extracted_address is None:
                    row['Final Remarks'] = "Address missing in aadhar"
                elif extracted_name is None:
                    row['Final Remarks'] = "Name missing in aadhar"
                else:
                    row['Final Remarks'] = "Non Aadhar"

            row["Document Type"] = "Aadhaar" if overall_match else "Non-Aadhaar"
        else:
            row.replace(float('nan'), 0)
            row['Final Remarks'] = "Non Aadhar"
            row['Document Type'] = "Non Aadhar"
        excel_data.loc[idx] = row
    return excel_data

def create_visualizations(comparison_results):
    visualization_data = {}

    # TODO: Implement your visualization logic here

    # Example: Frequency of 'Final Remarks' (for a bar chart)
    visualization_data['final_remarks_frequency'] = {
        'labels': comparison_results['Final Remarks'].value_counts().index.tolist(),
        'values': comparison_results['Final Remarks'].value_counts().values.tolist()
    }

    # 2. Document Type Proportion (Pie Chart)
    visualization_data['document_type_proportion'] = {
        'labels': comparison_results['Document Type'].value_counts().index.tolist(),
        'values': comparison_results['Document Type'].value_counts().values.tolist()
    }

    # 3. Accepted vs. Rejected Proportion (Pie Chart)
    visualization_data['accepted_rejected_proportion'] = {
        'labels': comparison_results['Accepted/Rejected'].value_counts().index.tolist(),
        'values': comparison_results['Accepted/Rejected'].value_counts().values.tolist()
    }

    # 4. UID Match Score Distribution (Histogram) 
    visualization_data['uid_match_score_distribution'] = {
        'values': comparison_results['UID Match Score'].tolist() 
    }

    # 5. Name Match Score Distribution (Histogram)
    visualization_data['name_match_score_distribution'] = {
        'values': comparison_results['Name Match Score'].tolist()
    }

    # 6. Final Address Match Score Distribution (Histogram)
    visualization_data['address_match_score_distribution'] = {
        'values': comparison_results['Final Address Match Score'].tolist()
    }

    return visualization_data

def create_database_and_table():
    """Creates the database and table if they don't exist."""
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            SrNo TEXT,
            DocumentType TEXT,
            AcceptedRejected TEXT,
            FinalRemarks TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_results_to_database(results):
    """Saves the provided results to the SQLite database."""
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()

    for result in results:
        cursor.execute('''
            INSERT INTO results (SrNo, DocumentType, AcceptedRejected, FinalRemarks)
            VALUES (?, ?, ?, ?)
        ''', (
            result.get('SrNo', ''), 
            result.get('Document Type', ''), 
            result.get('Accepted/Rejected', ''), 
            result.get('Final Remarks', '')
        ))
    
    conn.commit()
    conn.close()



@app.route('/download', methods=['GET'])
def download_results():
    file_path = os.path.join(app.config['RESULTS_FOLDER'], 'results.xlsx')
    return send_file(file_path, as_attachment=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'zipfile' in request.files and 'excelfile' in request.files:
        zip_file = request.files['zipfile']
        excel_file = request.files['excelfile']

        # Save files
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_file.filename)
        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_file.filename)
        zip_file.save(zip_path)
        excel_file.save(excel_path)

        # Unzip and process images
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(app.config['UPLOAD_FOLDER'])

        image_paths = [os.path.join(app.config['UPLOAD_FOLDER'], f) for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.endswith(('.jpg', '.png'))]
        processed_results = {}

        for image_path in image_paths:
            file_name = os.path.basename(image_path)
            key = file_name.split('.')[0][:3]
            if key not in processed_results:  # Check if key already exists
                extracted_data = process_image(image_path)
                if extracted_data:
                    processed_results[key] = extracted_data

        # Read Excel and compare data
        df = pd.read_excel(excel_path)
        df = df.astype('str')
        comparison_results = compare_data(df, processed_results)
        comparison_results['Accepted/Rejected'] = np.where(comparison_results['Final Remarks'] == 'All matched', 'Accepted', 'Rejected')

        # Save results to a new Excel file
        results_df = pd.DataFrame(comparison_results)
        os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)
        results_file_path = os.path.join(app.config['RESULTS_FOLDER'], 'results.xlsx')
        results_df.to_excel(results_file_path, index=False)

        visualization_data = create_visualizations(comparison_results)

        create_database_and_table() # Ensure database and table exist
        save_results_to_database(comparison_results[
                        ['SrNo', 'Document Type', 'Accepted/Rejected', 'Final Remarks']
                    ].to_dict(orient='records'))

        return jsonify({"message": "Files processed successfully!", 
                    "results": comparison_results[
                        ['SrNo', 'Document Type', 'Accepted/Rejected', 'Final Remarks']
                    ].to_dict(orient='records'),
                    "visualization_data": visualization_data})  

    return jsonify({"error": "Both files are required."}), 400

if __name__ == '__main__':
    # Configure HTTPS with self-signed certificate
    app.run(debug=True)
