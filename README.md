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

## ⚠️ Language Support

This app uses Tesseract OCR with support for **both English and Spanish**.  
Make sure your Tesseract installation includes the following language data files:

- `eng.traineddata` (included by default)
- `spa.traineddata` (**must be downloaded manually if not present**)

To install Spanish language support, download `spa.traineddata` from the official repo:  
https://github.com/tesseract-ocr/tessdata

Place the file inside the `tessdata` folder of your Tesseract installation directory.

---

## Installation Steps

### 1. Install Tesseract OCR

- Download the Windows installer from:  
  https://github.com/UB-Mannheim/tesseract/wiki
- Install it to:  
  `C:\Tesseract-OCR` or a similar folder
- Copy the full path to `tesseract.exe` for later use
- Make sure the folder `tessdata/` includes `spa.traineddata` (for Spanish).

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
```

---

## Running the App (from Python)

To use the application from source:

1. Make sure Python and all dependencies are installed.
2. Open a terminal in the project directory.
3. Run the script:

```bash
python ocr_pdf.py
```

4. A file picker window will appear. Select a scanned PDF file.
5. The extracted text will be saved to texto_extraido.txt and opened automatically.

---

## Building the Executable (.exe)
You can compile the project as a portable .exe using PyInstaller.

1. Project Structure Required
Your project folder should look like this:

```bash
ocr_pdf/
├── ocr_pdf.py
├── README.md
├── requirements.txt
├── Tesseract-OCR/
│   └── tesseract.exe, tessdata/, etc.
└── poppler/
    └── Library/
        └── bin/
            └── pdfinfo.exe, other DLLs...
```

---

2. Run PyInstaller
Inside the ocr_pdf folder, run:

```bash
pyinstaller --onefile ^
  --add-data "Tesseract-OCR;Tesseract-OCR" ^
  --add-data "poppler\\Library\\bin;poppler\\Library\\bin" ^
  ocr_pdf.py
```

Notes:
The --add-data argument ensures all necessary binaries are included.
The resulting executable will be created in the dist/ folder as ocr_pdf.exe.

---

## Distributing the Executable
You can share the .exe file from dist/ directly. The end user can:

1. Double-click to open the application.
2. Select a PDF file.
3. Receive the extracted text in a plain .txt file, opened automatically.

No Python, Tesseract, or Poppler installations are needed on the target machine.

---

## Project Folder Structure (Summary)

```bash
ocr_pdf/
├── ocr_pdf.py
├── README.md
├── requirements.txt
├── .gitignore
├── Tesseract-OCR/        # Not committed to GitHub
└── poppler/              # Not committed to GitHub
```

---

This application was developed for a freelance client who needed to extract Spanish-language text from scanned PDF documents. The final product is a self-contained .exe that works on any Windows machine and outputs the OCR results to a text file with no installation required.
