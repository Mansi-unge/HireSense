import PyPDF2

def extract_resume_text(pdf_path):
    """
    Extracts text from a resume PDF file.
    Returns lowercase plain text.
    """
    text = ""

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

    return text.lower()
