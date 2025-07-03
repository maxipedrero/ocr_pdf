# OCR PDF Extractor

This is a Python-based application for extracting text from scanned PDF files. It uses Tesseract OCR and Poppler to process each page, and outputs the recognized text to a `.txt` file. The tool includes a simple file selector and displays progress in the terminal. It's also packaged as a standalone `.exe` using PyInstaller, so it can run on any Windows machine without requiring Python or additional installations.

---

## Features

- Converts scanned PDF pages to images using Poppler
- Extracts text using Tesseract OCR (supports Spanish)
- Displays progress using a terminal progress bar
- Saves the extracted text to `texto_extraido.txt`
- Automatically opens the text file after processing
- Can be compiled into a single-file `.exe`

---

## Requirements (for development)

- Python 3.8 or later
- Tesseract OCR (installed locally)
- Poppler for Windows
- Python packages: `pytesseract`, `pdf2image`, `tqdm`
- `spa.traineddata` file for Spanish OCR

---

## Installation Steps

### 1. Install Tesseract OCR

- Download the Windows installer from:  
  https://github.com/UB-Mannheim/tesseract/wiki
- Install it to:  
  `C:\Tesseract-OCR` or a similar folder
- Copy the full path to `tesseract.exe` for later use
- Make sure the folder `tessdata/` includes `spa.traineddata` (for Spanish).  
  If not, download it from:  
  https://github.com/tesseract-ocr/tessdata

### 2. Install Poppler for Windows

- Download from:  
  https://github.com/oschwartz10612/poppler-windows/releases/
- Extract it to a folder such as:  
  `C:\poppler`
- The path to use in code is:  
  `C:\poppler\Library\bin`

### 3. Install Python dependencies

```bash
pip install pytesseract pdf2image tqdm
