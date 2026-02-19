import PyPDF2
import docx
import os

def extract_resume_text(file_path):
    """
    Extracts raw text from a resume file (PDF or DOCX).

    Parameters:
        file_path (str): Path to the resume file.

    Returns:
        str: Extracted text in lowercase. Returns empty string if extraction fails.
    """

    text = ""
    ext = os.path.splitext(file_path)[1].lower()  # Get the file extension

    try:
        # Handle PDF files
        if ext == ".pdf":
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)  # Initialize PDF reader
                for page in reader.pages:
                    # Extract text if available
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + " "

        # Handle DOCX files
        elif ext == ".docx":
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text + " "

    except Exception:
        # If any error occurs (corrupt file, unreadable format), return empty string
        return ""

    # Convert to lowercase to standardize for further processing
    return text.lower()
