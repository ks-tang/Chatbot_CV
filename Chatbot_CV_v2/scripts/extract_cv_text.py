import fitz  # PyMuPDF

def pdf_to_text(pdf_path, txt_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

# Exemple d'utilisation
pdf_to_text("../data/documents/CV_KevinTANG_v4.pdf", "../data/documents/cv.txt")
