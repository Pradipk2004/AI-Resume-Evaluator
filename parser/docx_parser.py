import docx

def extract_text_from_docx(file_path_or_bytes):
    doc = docx.Document(file_path_or_bytes)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text).strip()