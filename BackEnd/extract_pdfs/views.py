from django.http import HttpResponse
from extract_pdfs import prosecution
from db.models import Records
from django.core import serializers
import json

def db_data(request):
    table_name=request.GET['table_name']
    # Ordenamos descendentemente.
    if table_name == 'EXTRACTION':
        r = serializers.serialize('json', Records.objects.order_by('-id'))
        return HttpResponse(r)
    else:
        return HttpResponse(json.dumps([[False, 2], "Base de datos no encontrada"], indent=4))
def extract(request):

    doc_path=request.GET['doc_path']
    
    # Obtenemos los datos que vamos a extraer de la imagen en pdf
    pdf = prosecution.extract_from_pdf(doc_path)

    # if pdf no es None es porque extrajo las palabras claves que necesitamos 
    if pdf is not None:
        # Serializamos dichos archivos y luego lo guardamos en la base de datos  
        record = Records(**pdf)
        record.save()
        # Agragamos la ruta al request
        pdf['Doc_Path'] = doc_path
        return HttpResponse(json.dumps([[True, 2], pdf], indent=4))
    else:
        return HttpResponse(json.dumps([[False, 2], "Documento no encontrado en la máquina local"], indent=4))
