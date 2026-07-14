# Film Dosimetry Calculator

### Calibration Curve and GUI Development for Radiochromic Film Dosimetry

## Overview

The **Film Dosimetry Calculator** is a Python-based desktop application developed during my internship at **Apollo Multispeciality Hospitals, Kolkata**. The software is designed to automate dose estimation from scanned radiochromic film images used in radiotherapy quality assurance (QA).

The application processes TIFF images, extracts pixel information from a defined region of interest (ROI), and calculates radiation dose using a pre-calibrated film dosimetry equation. Results are displayed in a user-friendly graphical interface and can be exported for further analysis.

---

## Project Objectives

* Develop a calibration model relating film pixel values to delivered radiation dose.
* Automate dose estimation from scanned radiochromic film images.
* Create a user-friendly desktop application for clinical and research use.
* Eliminate manual calculations and reduce processing time.
* Generate exportable reports for documentation and analysis.

---

## Features

✅ Simple graphical user interface (GUI)

✅ Batch processing of multiple TIFF images

✅ Automatic extraction of central Region of Interest (ROI)

✅ Mean pixel value calculation

✅ Dose prediction using calibration equation

✅ Results displayed in tabular format

✅ CSV export functionality

✅ Standalone executable deployment using PyInstaller

✅ No external calibration file required (calibration constants embedded)

---

## Technology Stack

| Component             | Technology   |
| --------------------- | ------------ |
| Programming Language  | Python       |
| GUI Framework         | Tkinter      |
| Image Processing      | Pillow (PIL) |
| Numerical Computation | NumPy        |
| Data Export           | Pandas       |
| Packaging             | PyInstaller  |

---

## Calibration Model

The calibration curve was obtained using scanned radiochromic films irradiated at known dose levels.

### Calibration Constants

| Parameter | Value      |
| --------- | ---------- |
| a         | 19.6337    |
| b         | 13278.6836 |
| c         | 122.7532   |

### Dose Prediction Equation

[
Dose = \frac{b}{(Pixel - a)} - c
]

where:

* **Pixel** = Mean red-channel pixel value from ROI
* **Dose** = Predicted radiation dose (cGy)

---

## Workflow

### Step 1: Select TIFF Folder

The user selects a folder containing scanned radiochromic film images.

### Step 2: Image Processing

For each image:

1. Load TIFF image
2. Extract central 200 × 200 pixel ROI
3. Calculate mean red-channel value
4. Apply calibration equation
5. Predict dose

### Step 3: Results Display

Results are displayed in a table containing:

* File Name
* Mean Pixel Value
* Predicted Dose (cGy)

### Step 4: Export Results

Results can be exported as a CSV file for documentation and further analysis.

---

## GUI Preview

The GUI provides:

* Folder Selection
* Dose Calculation
* Results Table
* CSV Export

### Output Table

| File Name | Mean Pixel | Predicted Dose (cGy) |
| --------- | ---------- | -------------------- |
| 250.tif   | 53.99      | 263.79               |
| 550.tif   | 37.31      | 628.53               |
| 600.tif   | 36.92      | 645.54               |

---

## Project Structure

```text
FilmDosimetryCalculator/
│
├── film_dosimetry_gui.py
├── README.md
├── dist/
│   └── FilmDosimetryCalculator.exe
│
└── sample_output/
    └── dose_results.csv
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/film-dosimetry-calculator.git

cd film-dosimetry-calculator
```

### Install Dependencies

```bash
pip install numpy pandas pillow
```

### Run Application

```bash
python film_dosimetry_gui.py
```

---

## Building Executable

Generate a standalone Windows executable using:

```bash
pyinstaller --onefile --windowed film_dosimetry_gui.py
```

The executable will be created inside:

```text
dist/
```

---

## Applications

This software can be used for:

* Radiotherapy Quality Assurance (QA)
* Film Dosimetry Analysis
* Fluence Verification
* Radiation Dose Measurement
* Medical Physics Research
* Educational Demonstrations

---

## Internship Information

**Organization:** Apollo Multispeciality Hospitals, Kolkata

**Project Title:** Film Dosimetry Calculator: Calibration Curve and GUI Development

**Duration:** May 25, 2026 – June 30, 2026

The developed software has applications in radiotherapy quality assurance and has been implemented for film dosimetry-based fluence verification within the Department of Radiotherapy at Apollo Multispeciality Hospitals. 

---

## Author

**Enakshy Mondal**

B.Tech Computer Science Engineering

KIIT University

---

## Acknowledgements

Special thanks to:

**Dr. Biplab Sarkar, Ph.D.**
Chief Medical Physicist & Radiation Safety Officer (RSO)
Apollo Multispeciality Hospitals, Kolkata

for guidance, mentorship, and support throughout the project. 
