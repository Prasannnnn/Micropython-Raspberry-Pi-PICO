import os
import fitz  # PyMuPDF
from PIL import Image

def convert_cbr_to_pdf(cbr_path, pdf_path):
    # Open the CBR file
    images = []
    for root, _, files in os.walk(cbr_path):
        for file in sorted(files):
            if file.endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(root, file)
                images.append(Image.open(img_path))

    # Create a PDF
    if images:
        pdf_document = fitz.open()
        for image in images:
            img_byte_arr = image.tobytes()
            img_pdf = fitz.open("pdf", img_byte_arr)
            pdf_document.insert_pdf(img_pdf)
        pdf_document.save(pdf_path)
        pdf_document.close()

def batch_convert_cbr_to_pdf(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) and item.endswith('.cbr'):
            pdf_filename = os.path.splitext(item)[0] + '.pdf'
            pdf_path = os.path.join(folder_path, pdf_filename)
            convert_cbr_to_pdf(item_path, pdf_path)

# Specify the folder containing CBR files
folder_path = r'D:\Prasanna\The Boys (Collection) (2006-2012)\01. The Boys 001-072+ (2006-2012)'
batch_convert_cbr_to_pdf(folder_path)
