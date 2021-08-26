from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import re

to_find = {"Vendor name:": ["Vendor (Name|name):\D+\n", "VendorName", "Vendor Name:"],
            "Fiscal number:": ["Fiscal (number|Number):.\d+.\d+.\d+", "FiscalNumber", "Fiscal Number:"],
            "Contract#:": ["Contract(#| #):.\d+", "ContractNumbe", "Contract #:"],
            "Start date:": ["Start date:(\n?)*\d+/\d+/\d+", "StartDate"],
            "End date:": ["End date:.*\d+/\d+/\d+", "EndDate"],
            "Comments:": ["Comments:(\n*\D+(\.\n)|\n)", "CommPph"]}

PathImagen = '/project/extract_pdfs/images/' 

def extract_from_pdf(url):

    try:
        pages = convert_from_path(url)
    except:
        return None

    # guardamos cada imagen en la ruta actual
    for page in pages:
        page.save(PathImagen + 'out.png', 'PNG')

    # Abrimos la imagen
    im = Image.open(PathImagen + 'out.png')

    # Utilizamos el método "image_to_string"
    # Le pasamos como argumento la imagen abierta con Pillow
    tx = pytesseract.image_to_string(im)
    dict_text = {}

    for key, value in to_find.items():
        Value = re.search("{}".format(value[0]), tx)

        if Value is None:
            continue

        Value = Value.group()

        if (Value.startswith(key)):
            Value = Value.strip(key)
        else:
            Value = Value.strip(value[2])
        Value = Value.strip('\n')

        dict_text[value[1]] = Value

    im.close()

    return dict_text
