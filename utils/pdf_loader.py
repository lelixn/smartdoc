from PyPDF2 import PdfReader


def load_pdf(file) -> str:
    """
    Extracts text from an uploaded PDF file.

    Args:
        file: Streamlit uploaded file object

    Returns:
        Combined text from all pages
    """
    reader = PdfReader(file)
    full_text = []

    for page_num, page in enumerate(reader.pages):
        try:
            text = page.extract_text()
            if text:
                # Clean excessive whitespace
                text = " ".join(text.split())
                full_text.append(text)
        except Exception as e:
            print(f"⚠️ Error reading page {page_num}: {e}")

    return "\n".join(full_text)
