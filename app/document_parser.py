import pdfplumber

def extract_text(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    else:
        text = uploaded_file.read().decode("utf-8")
    return text
