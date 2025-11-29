# Product Vision Data Pipeline

## Overview

An AI-powered pipeline that converts unstructured product images into structured data (YAML). This tool leverages Computer Vision and Large Language Models (LLMs) to extract attributes like brand, size, and packaging details automatically, streamlining cataloging operations for e-commerce.

## Tech Stack

- **Language:** Python 3.8+
- **Vision Model:** Google Gemini 2.0 Flash (via API)
- **Image Processing:** OpenCV, Pillow
- **Data Handling:** PyYAML

## Project Structure

```text
product-vision-pipeline/
├── data/
│   ├── input_images/       # Place raw product images here
│   └── output_yaml/        # Generated structured data appears here
├── src/
│   ├── extractor.py        # Handles API communication with Vision Model
│   ├── preprocessor.py     # Resizes and denoises images
│   └── utils.py            # Helper functions for file I/O
├── .env                    # API keys (Not tracked in Git)
├── main.py                 # Entry point of the application
└── requirements.txt        # Python dependencies

```

## Setup & Installation

### 1. Clone the repository

```bash
git clone [https://github.com/sanayaparmar/product-vision-pipeline.git](https://github.com/sanayaparmar/product-vision-pipeline.git)
cd product-vision-pipeline
2. Install Dependencies
pip install -r requirements.txt
3. Configure API Key
Create a file named .env in the root directory.
Add your Google Gemini API key:
GEMINI_API_KEY=GEMINI_API_KEY=your_actual_api_key_here
Usage
Add Images: Place your product images (JPG, PNG) into the data/input_images/ folder.
Run the Pipeline:
python main.py
View Results: Check the data/output_yaml/ folder for the extracted data files.

Key Features
Smart Preprocessing: Automatically resizes and applies noise reduction to improve OCR accuracy.
Robust Extraction: Identifies Brand, Volume, Pack Size, and key marketing claims.
Error Handling: Built-in retry logic for file system operations and API connectivity.
```
