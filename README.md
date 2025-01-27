<div align="left" style="position: relative;">
<h1>AI BASED AADHAR_FRAUD_MANAGEMENT</h1>
<p align="left">
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/ShutterStack/Aadhar_Fraud_Management?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/ShutterStack/Aadhar_Fraud_Management?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ShutterStack/Aadhar_Fraud_Management?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ShutterStack/Aadhar_Fraud_Management?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

## Overview

This project implements a sophisticated Aadhaar fraud detection and management system, leveraging state-of-the-art AI and computer vision technologies to fortify the security and integrity of Aadhaar-based verification workflows. The system tackles the challenge of automating the extraction and validation of crucial information from Aadhaar card images, enabling efficient fraud detection and identity verification.

**Technical Implementation:**

* **Object Detection and OCR:** The core of the system is powered by a pre-trained YOLOv8 object detection model (located in the `detection_model` folder), carefully trained to identify and extract specific regions of interest (ROIs) from Aadhaar cards, including Name, UID, and Address fields. Extracted ROIs are then processed using the EasyOCR library, an open-source OCR engine, for converting text within the images into machine-readable text.

* **Fuzzy Matching:** To ensure robust comparison even with potential variations in data entry, OCR results, or image quality, the system utilizes FuzzyWuzzy, a Python library renowned for its fuzzy string matching capabilities. This allows the system to accommodate minor discrepancies and deliver accurate verification results. 

* **Flask Web Framework:** The backend functionality is built using Flask, a lightweight and versatile Python web framework. Flask enables the creation of a RESTful API for handling file uploads (Aadhaar images in a zip archive and Excel files with reference data), orchestrating the data extraction and comparison pipeline, and generating results.

* **Frontend and Visualizations:** The user interface is implemented with HTML, CSS, and JavaScript, providing a clean and intuitive experience. Processed results are presented using interactive visualizations generated with Chart.js, a powerful JavaScript charting library. These visualizations encompass bar charts, pie charts, and histograms, offering insights into data accuracy, potential fraud indicators, and system performance metrics. 

**Benefits:**

* **Automation:** Streamlines the traditionally manual and time-consuming process of Aadhaar verification, significantly reducing human effort and potential for error.
* **Accuracy:** Utilizes a combination of precise object detection, accurate OCR, and robust fuzzy matching algorithms to ensure reliable data extraction and verification results.
* **Scalability:** The system's modular design and utilization of Flask as the backend framework allow for scalability to handle large volumes of Aadhaar data. 
* **Actionable Insights:** Interactive visualizations empower users to gain valuable insights from the processed data, facilitating informed decision-making in fraud prevention and identity verification. 


---

##  Features

#### 1)Automated Aadhaar Data Extraction:
Leverages a pre-trained YOLOv8 object detection model to precisely locate and extract key data fields from Aadhaar cards, including Name, UID (Unique Identification Number), and Address components. This automated extraction process minimizes manual effort and ensures data accuracy.
   
#### 2) Advanced OCR Capabilities: 
Employs the EasyOCR library, an open-source OCR engine, to convert the text within the detected regions of interest from image format to machine-readable text. This enables the system to process and analyze the extracted Aadhaar information.
#### 3) Intelligent Data Comparison: 
Implements FuzzyWuzzy, a Python library for fuzzy string matching, to compare the extracted Aadhaar data with reference datasets. The use of fuzzy matching techniques accommodates potential variations in data entry, OCR output, or image quality, resulting in robust and reliable verification even with minor discrepancies.
#### 4) Comprehensive Fraud Detection: 
Identifies potential fraud attempts by rigorously comparing the extracted Aadhaar information against trusted datasets, flagging any inconsistencies, and highlighting suspicious patterns for further investigation.
#### 5) User-Friendly Web Interface:  
Provides an intuitive web-based platform built with Flask, HTML, CSS, and JavaScript, enabling users to easily upload zip files containing Aadhaar images and Excel spreadsheets with corresponding reference data. The interface also facilitates seamless process initiation and result download.
#### 6) Interactive Data Visualizations:  
Presents the processed results using Chart.js, a JavaScript charting library, to generate insightful bar charts, pie charts, and histograms. These visualizations offer users a clear, concise understanding of data accuracy, potential fraud indicators, and overall system performance.
#### 7) Seamless System Integration:  
Designed for easy integration into existing systems and workflows, streamlining verification processes and fortifying security protocols within organizations.


![ FlowChart ](https://github.com/user-attachments/assets/46c1583e-e7f3-46aa-9c82-4a86a3b99690)

---

###  Project Index
<details open>
	<summary><b><code>AADHAR_FRAUD_MANAGEMENT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/vercel.json'>vercel.json</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/app.py'>app.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- Base Models Submodule -->
		<summary><b>Base Models</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/yolo11n-cls.pt'>yolo11n-cls.pt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>ocr</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/ocr/ocr.ipynb'>ocr.ipynb</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>.ipynb_checkpoints</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/ocr/.ipynb_checkpoints/ocr-checkpoint.ipynb'>ocr-checkpoint.ipynb</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>runs</b></summary>
				<blockquote>
					<details>
						<summary><b>classify</b></summary>
						<blockquote>
							<details>
								<summary><b>train</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/runs/classify/train/args.yaml'>args.yaml</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
									<details>
										<summary><b>weights</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/runs/classify/train/weights/best.pt'>best.pt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/runs/classify/train/weights/last.pt'>last.pt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>detection_model</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/data.yaml'>data.yaml</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/yolo11n.pt'>yolo11n.pt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/detection_model.ipynb'>detection_model.ipynb</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>dataset</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/classes.txt'>classes.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>labels</b></summary>
								<blockquote>
									<details>
										<summary><b>val</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/266.txt'>266.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/286.txt'>286.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/242.txt'>242.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/276.txt'>276.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/273.txt'>273.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/252.txt'>252.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/267.txt'>267.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/291.txt'>291.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/284.txt'>284.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/290.txt'>290.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/262.txt'>262.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/260.txt'>260.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/271.txt'>271.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/289.txt'>289.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/259.txt'>259.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/272.txt'>272.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/283.txt'>283.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/250.txt'>250.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/246.txt'>246.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/275.txt'>275.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/270.txt'>270.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/264.txt'>264.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/274.txt'>274.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/248.txt'>248.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/269.txt'>269.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/261.txt'>261.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/253.txt'>253.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/268.txt'>268.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/257.txt'>257.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/277.txt'>277.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/278.txt'>278.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/245.txt'>245.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/279.txt'>279.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/247.txt'>247.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/281.txt'>281.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/287.txt'>287.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/241.txt'>241.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/251.txt'>251.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/258.txt'>258.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/282.txt'>282.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/265.txt'>265.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/255.txt'>255.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/288.txt'>288.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/263.txt'>263.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/249.txt'>249.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/285.txt'>285.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/244.txt'>244.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/254.txt'>254.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/280.txt'>280.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/243.txt'>243.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/val/256.txt'>256.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>train</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/86.txt'>86.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/60.txt'>60.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/37.txt'>37.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/134.txt'>134.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/167.txt'>167.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/213.txt'>213.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/99.txt'>99.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/198.txt'>198.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/131.txt'>131.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/71.txt'>71.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/211.txt'>211.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/231.txt'>231.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/119.txt'>119.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/95.txt'>95.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/164.txt'>164.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/208.txt'>208.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/121.txt'>121.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/28.txt'>28.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/206.txt'>206.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/133.txt'>133.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/190.txt'>190.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/189.txt'>189.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/226.txt'>226.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/221.txt'>221.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/138.txt'>138.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/104.txt'>104.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/27.txt'>27.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/72.txt'>72.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/222.txt'>222.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/93.txt'>93.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/101.txt'>101.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/52.txt'>52.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/228.txt'>228.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/89.txt'>89.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/149.txt'>149.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/143.txt'>143.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/66.txt'>66.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/227.txt'>227.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/57.txt'>57.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/74.txt'>74.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/172.txt'>172.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/108.txt'>108.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/197.txt'>197.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/201.txt'>201.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/1.txt'>1.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/238.txt'>238.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/30.txt'>30.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/70.txt'>70.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/181.txt'>181.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/117.txt'>117.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/177.txt'>177.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/126.txt'>126.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/122.txt'>122.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/51.txt'>51.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/129.txt'>129.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/179.txt'>179.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/4.txt'>4.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/180.txt'>180.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/195.txt'>195.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/160.txt'>160.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/11.txt'>11.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/25.txt'>25.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/44.txt'>44.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/127.txt'>127.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/178.txt'>178.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/111.txt'>111.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/58.txt'>58.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/145.txt'>145.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/13.txt'>13.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/88.txt'>88.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/116.txt'>116.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/67.txt'>67.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/109.txt'>109.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/62.txt'>62.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/113.txt'>113.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/183.txt'>183.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/225.txt'>225.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/8.txt'>8.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/45.txt'>45.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/135.txt'>135.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/97.txt'>97.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/174.txt'>174.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/69.txt'>69.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/10.txt'>10.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/120.txt'>120.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/107.txt'>107.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/218.txt'>218.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/187.txt'>187.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/216.txt'>216.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/161.txt'>161.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/156.txt'>156.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/63.txt'>63.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/193.txt'>193.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/137.txt'>137.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/153.txt'>153.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/229.txt'>229.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/114.txt'>114.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/22.txt'>22.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/49.txt'>49.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/84.txt'>84.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/163.txt'>163.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/106.txt'>106.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/42.txt'>42.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/236.txt'>236.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/9.txt'>9.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/176.txt'>176.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/39.txt'>39.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/186.txt'>186.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/12.txt'>12.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/94.txt'>94.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/61.txt'>61.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/125.txt'>125.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/14.txt'>14.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/173.txt'>173.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/81.txt'>81.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/205.txt'>205.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/82.txt'>82.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/240.txt'>240.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/130.txt'>130.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/15.txt'>15.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/124.txt'>124.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/18.txt'>18.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/76.txt'>76.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/110.txt'>110.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/148.txt'>148.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/136.txt'>136.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/91.txt'>91.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/215.txt'>215.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/24.txt'>24.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/2.txt'>2.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/65.txt'>65.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/98.txt'>98.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/5.txt'>5.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/80.txt'>80.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/224.txt'>224.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/235.txt'>235.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/105.txt'>105.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/141.txt'>141.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/43.txt'>43.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/154.txt'>154.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/6.txt'>6.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/152.txt'>152.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/140.txt'>140.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/87.txt'>87.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/194.txt'>194.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/212.txt'>212.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/56.txt'>56.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/162.txt'>162.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/150.txt'>150.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/165.txt'>165.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/234.txt'>234.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/142.txt'>142.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/203.txt'>203.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/237.txt'>237.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/185.txt'>185.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/102.txt'>102.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/17.txt'>17.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/217.txt'>217.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/46.txt'>46.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/232.txt'>232.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/209.txt'>209.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/123.txt'>123.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/192.txt'>192.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/144.txt'>144.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/175.txt'>175.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/155.txt'>155.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/54.txt'>54.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/32.txt'>32.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/40.txt'>40.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/68.txt'>68.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/158.txt'>158.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/157.txt'>157.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/223.txt'>223.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/21.txt'>21.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/169.txt'>169.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/188.txt'>188.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/210.txt'>210.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/168.txt'>168.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/184.txt'>184.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/170.txt'>170.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/96.txt'>96.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/100.txt'>100.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/207.txt'>207.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/29.txt'>29.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/19.txt'>19.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/103.txt'>103.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/196.txt'>196.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/214.txt'>214.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/199.txt'>199.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/146.txt'>146.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/55.txt'>55.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/83.txt'>83.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/53.txt'>53.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/79.txt'>79.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/20.txt'>20.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/132.txt'>132.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/16.txt'>16.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/47.txt'>47.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/50.txt'>50.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/219.txt'>219.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/220.txt'>220.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/38.txt'>38.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/77.txt'>77.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/182.txt'>182.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/128.txt'>128.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/151.txt'>151.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/239.txt'>239.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/35.txt'>35.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/171.txt'>171.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/41.txt'>41.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/26.txt'>26.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/75.txt'>75.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/23.txt'>23.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/90.txt'>90.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/85.txt'>85.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/112.txt'>112.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/78.txt'>78.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/34.txt'>34.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/233.txt'>233.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/115.txt'>115.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/118.txt'>118.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/200.txt'>200.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/230.txt'>230.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/166.txt'>166.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/147.txt'>147.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/48.txt'>48.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/92.txt'>92.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/36.txt'>36.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/159.txt'>159.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/33.txt'>33.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/139.txt'>139.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/202.txt'>202.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/59.txt'>59.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/31.txt'>31.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/3.txt'>3.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/64.txt'>64.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/7.txt'>7.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/73.txt'>73.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/204.txt'>204.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/dataset/labels/train/191.txt'>191.txt</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>runs</b></summary>
						<blockquote>
							<details>
								<summary><b>detect</b></summary>
								<blockquote>
									<details>
										<summary><b>train2</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/runs/detect/train2/args.yaml'>args.yaml</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
											<details>
												<summary><b>weights</b></summary>
												<blockquote>
													<table>
													<tr>
														<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/runs/detect/train2/weights/best.pt'>best.pt</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/runs/detect/train2/weights/last.pt'>last.pt</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<details>
										<summary><b>train</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/runs/detect/train/args.yaml'>args.yaml</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>.ipynb_checkpoints</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/detection_model/.ipynb_checkpoints/detection_model-checkpoint.ipynb'>detection_model-checkpoint.ipynb</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>classification_model</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/Base Models/classification_model/Classification.ipynb'>Classification.ipynb</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- templates Submodule -->
		<summary><b>templates</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/templates/about.html'>about.html</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/templates/index.html'>index.html</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/templates/contact.html'>contact.html</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/templates/services.html'>services.html</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- models Submodule -->
		<summary><b>models</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/models/classification.pt'>classification.pt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/master/models/detection.pt'>detection.pt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with Aadhar_Fraud_Management, ensure your runtime environment meets the following requirements:

###  Installation

Install Aadhar_Fraud_Management using one of the following methods:

**Build from source:**

1. Clone the Aadhar_Fraud_Management repository:
```sh
git clone https://github.com/ShutterStack/Aadhar_Fraud_Management
```

2. Navigate to the project directory:
```sh
cd Aadhar_Fraud_Management
```

3. Install the project dependencies:


**Set up environnment first and enable env

```sh
python -m venv venv
venv/Scripts/Activate
```


###  Requirements
Run Aadhar_Fraud_Management using the following command:
**First install all the requirements

```sh
pip install -r requirements.txt
```


### Running and Debugging
Run the test suite using the following command:
```sh
python app.py
```


---
##  Contributing

- **💬 [Join the Discussions](https://github.com/ShutterStack/Aadhar_Fraud_Management/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/ShutterStack/Aadhar_Fraud_Management/issues)**: Submit bugs found or log feature requests for the `Aadhar_Fraud_Management` project.
- **💡 [Submit Pull Requests](https://github.com/ShutterStack/Aadhar_Fraud_Management/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ShutterStack/Aadhar_Fraud_Management
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/ShutterStack/Aadhar_Fraud_Management/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ShutterStack/Aadhar_Fraud_Management">
   </a>
</p>
</details>

---
