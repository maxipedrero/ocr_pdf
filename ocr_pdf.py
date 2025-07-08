import sys
import os
import pytesseract
from pdf2image import convert_from_path
from tkinter import Tk, filedialog
from tqdm import tqdm

try:
    print("📂 Iniciando programa...")

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()

    tesseract_path = os.path.join(base_path, 'Tesseract-OCR', 'tesseract.exe')
    poppler_path = os.path.join(base_path, 'poppler', 'Library', 'bin')

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    root = Tk()
    root.withdraw()
    print("🗂 Seleccioná un archivo PDF...")
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if not pdf_path:
        print("❌ No se seleccionó ningún archivo.")
        input("Presioná Enter para salir...")
        sys.exit()

    print(f"📄 PDF seleccionado: {pdf_path}")
    print("🖼 Convirtiendo PDF a imágenes...")
    paginas = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    print(f"✅ Total de páginas: {len(paginas)}")

    texto_total = ""
    print("🔍 Iniciando OCR...")

    for i, pagina in enumerate(tqdm(paginas, desc="Procesando páginas", unit="pág")):
        texto = pytesseract.image_to_string(pagina, lang='spa')
        texto_total += f"\n--- Página {i+1} ---\n{texto}"

    output_path = "texto_extraido.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(texto_total)

    print(f"✅ OCR completado. Texto guardado en '{output_path}'")

    # 🔓 Abrir archivo automáticamente
    os.startfile(output_path)

except Exception as e:
    print("❌ Ocurrió un error:")
    print(e)

finally:
    input("Presioná Enter para salir...")
    
import sys
import os
import pytesseract
from pdf2image import convert_from_path
from tkinter import Tk, filedialog
from tqdm import tqdm

try:
    print("📂 Iniciando programa...")

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()

    tesseract_path = os.path.join(base_path, 'Tesseract-OCR', 'tesseract.exe')
    poppler_path = os.path.join(base_path, 'poppler', 'Library', 'bin')

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    root = Tk()
    root.withdraw()
    print("🗂 Seleccioná un archivo PDF...")
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if not pdf_path:
        print("❌ No se seleccionó ningún archivo.")
        input("Presioná Enter para salir...")
        sys.exit()

    print(f"📄 PDF seleccionado: {pdf_path}")
    print("🖼 Convirtiendo PDF a imágenes...")
    paginas = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    print(f"✅ Total de páginas: {len(paginas)}")

    texto_total = ""
    print("🔍 Iniciando OCR...")

    for i, pagina in enumerate(tqdm(paginas, desc="Procesando páginas", unit="pág")):
        texto = pytesseract.image_to_string(pagina, lang='eng+spa')
        texto_total += f"\n--- Página {i+1} ---\n{texto}"

    output_path = "texto_extraido.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(texto_total)

    print(f"✅ OCR completado. Texto guardado en '{output_path}'")

    # 🔓 Abrir archivo automáticamente
    os.startfile(output_path)

except Exception as e:
    print("❌ Ocurrió un error:")
    print(e)

finally:
    input("Presioná Enter para salir...")
