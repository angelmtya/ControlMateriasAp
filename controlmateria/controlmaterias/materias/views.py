import os
import zipfile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from materias.forms import Directorio 


#@login_required(login_url="login")
def home(request):
    #  directorio = request.GET.get('carpeta')
    #  ruta = 
    
    #  contenido = os.listdir(ruta)
    #  csv = []
    #  for fichero in contenido:
    #      if os.path.isfile(os.path.join(ruta, fichero)) and fichero.endswith('.csv'):
    #         csv.append(fichero) 
    #         #print(imagenes)
    
    #  for archivo in csv:
    #     with open(archivo,"r") as archivo:
    #         print(archivo.read())
    
    if request.method == 'GET':
        return render(request,'index.html', {'form': Directorio()})
    else:
        # ruta=request.POST.get('carpeta') #Retorna la ruta del archivo
        # print(ruta)
        ruta_zip = "/home/angel/Escritorio/prueba.zip"
        archivo_zip = zipfile.ZipFile(ruta_zip, "r")
        #archivo_zip = zipfile.ZipFile(request.POST.get('carpeta'))
        try:
            print(archivo_zip.namelist())
            #archivo_zip.extractall(pwd=password, pat)
        except:
            pass
        archivo_zip.close()
        return render(request,'index.html', {'form': Directorio()})


def login_view(request):
    return render(request,'paginas/login.html')