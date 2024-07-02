from PyPDF2 import PdfReader

def load_pdf(file_path):
    """
    Reads the text content from a PDF file and returns it as a single string.

    Parameters:
    - file_path (str): The file path to the PDF file.

    Returns:
    - str: The concatenated text content of all pages in the PDF.
    """
    # Logic for reading the file  
    pdf_reader = PdfReader(file_path)

    # Iterate through all the pages of the PDF and extract text
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

pdf_text = load_pdf(file_path="pdf/Investments.pdf")