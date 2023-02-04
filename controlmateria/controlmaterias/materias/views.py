import pandas as pd
import xlrd 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage    
from django.conf import settings
from .forms import UploadFileForm
from django.shortcuts import render
from materias.models import Materia, Alumno, Aprobada





# def leerContenido(file):
  
#     print(file.name)    
#     # #nombre = dt['Nombre']
#     filename = file
#     print(filename)
#     lineas = file.readlines()

#     df = pd.read_excel(file)
#     df.info()
#     print(df)
 # for i in range(36):
    #     for j in range(16):
    #         print('-------------------------------- '+str(i)+' '+str(j)+'  '+str(df.iat[i,j])+' -------------------------------------------------------')
    #     print('\n')
   
    #df = df[df['Unnamed: 13'] == "APROBADA"]
    #df.to_excel('Prueba1.xlsx', index=False)
 


def leerContenido(file):
  
    filename = file
    lineas = file.readlines()
    df = pd.read_excel(file)
    nombre = df.columns.values[5]
    matricula = str(df.iat[0,5])
    df = df[df['Unnamed: 13'] == "APROBADA"]
    df= df['Unnamed: 4'].str.split(')',expand=True) 
    lista_materias = df[1].tolist()
    df = df[0].str.split('(',expand=True)
    claves_materia = df[1].tolist()
    agregar_alumno(matricula, nombre)
    agregar_materias(claves_materia,lista_materias)
    agregar_aprobadas(matricula,  claves_materia)
    

def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        print(file.name)     
        leerContenido(file)
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form':  UploadFileForm()})


# def agregar_aprobadas(matricula, claves_materia):
#     for x in range(0,len(claves_materia)):
#         clave_aprobada = Aprobada.objects.get(materia=claves_materia[x], alumno=matricula)
#         if not clave_aprobada:
#             Aprobada.objects.create(
#             matricula_alumno = matricula,
#             claves_materia = clave_aprobada[x]
#             )


 



def agregar_materias(clavesm, materias):
    for x in range(0,len(clavesm)):
        clave_materia = Materia.objects.filter(clave=clavesm[x])
        if not clave_materia:
            materia = Materia.objects.create(
            clave = clavesm[x],
            nombre = materias[x] 
            )
        
def agregar_alumno(matricula, nombre):
    clave_alumno = Alumno.objects.filter(matricula=matricula)
    if not clave_alumno:
        alumno = Alumno.objects.create(
        matricula = matricula,
        nombre = nombre
        )
 
def agregar_aprobadas(matricula, claves_materia):
    alumno = Alumno.objects.get(matricula=matricula)
    for x in range(0,len(claves_materia)):
        #clave_aprobada = Aprobada.objects.filter(matricula_alumno=alumno, materia_ap=claves_materia[x])
        #if Aprobada.objects.filter(matricula_alumno=alumno, materia_ap=claves_materia[x]).count() == 0:
            Aprobada.objects.create(
            matricula_alumno = alumno,
            materia_ap  = Materia.objects.get(clave=claves_materia[x])
            )
           
      

#def agregar_alumno(matricula, nombre):
#     clave_alumno = Alumno.objects.filter(matricula=matricula)
#     if not clave_alumno:
#         nombre_completo = nombre.split()
#         tam = len(nombre_completo)
#         alumno = Alumno.objects.create(
#         matricula = matricula,
#         nombre = nombre_completo[tam-1],
#         primer_apellido =  nombre_completo[tam-2]
#         )
#         print(str(tam)+" -------------------")
#         if(tam>2):
#            alumno.segundo_apellido = nombre_completo[0]




# def home(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         file = request.FILES['file']
#         #print(file.name)     
#         leerContenido(file)
   
#     else:
#         form = UploadFileForm()
#     return render(request, 'index.html', {'form':  UploadFileForm()})


# class ReporteExcel(TemplateView):
#      def get(self,request,*args,**kwargs):
#         campo = (request.GET.get('campo'))
#         query = Datos.objects.filter(estatus = campo)
#         wb = Workbook()
#         ws = wb.active 

#                 #Crear el título en la hoja
#         ws['B1'].alignment = Alignment(horizontal = "center",vertical = "center")
#         ws['B1'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") ) 
#         ws['B1'].fill = PatternFill(start_color = 'CCCCFF', end_color = 'CCCCFF', fill_type = "solid")
#         ws['B1'].font = Font(name = 'Calibri', size = 12, bold = True)
#         ws['B1'] = 'REPORTE EN EXCEL'

#             #Cambiar caracteristicas de las celdas
#         ws.merge_cells('B1:H1')

#         ws.row_dimensions[1].height = 25

#         ws.column_dimensions['B'].width = 20
#         ws.column_dimensions['C'].width = 20
#         ws.column_dimensions['D'].width = 20
#         ws.column_dimensions['E'].width = 20
#         ws.column_dimensions['F'].width = 20
#         ws.column_dimensions['G'].width = 20
#         ws.column_dimensions['H'].width = 20

#             #Crear la cabecera
#         ws['B3'].alignment = Alignment(horizontal = "center", vertical = "center")
#         ws['B3'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws['B3'].fill = PatternFill(start_color = '66CFCC', end_color = '66CFCC', fill_type = "solid")
#         ws['B3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['B3'] = 'NOMBRES'

#         ws['C3'].alignment = Alignment(horizontal = "center", vertical = "center")
#         ws['C3'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws['C3'].fill = PatternFill(start_color = '66CFCC', end_color = '66CFCC', fill_type = "solid")
#         ws['C3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['C3'] = 'CICLO'

#         ws['D3'].alignment = Alignment(horizontal = "center", vertical = "center")
#         ws['D3'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws['D3'].fill = PatternFill(start_color = '66CFCC', end_color = '66CFCC', fill_type = "solid")
#         ws['D3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['D3'] = 'MATERIA'

#         ws['E3'].alignment = Alignment(horizontal = "center", vertical = "center")
#         ws['E3'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws['E3'].fill = PatternFill(start_color = '66CFCC', end_color = '66CFCC', fill_type = "solid")
#         ws['E3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['E3'] = 'CALIF'

#         ws['F3'].alignment = Alignment(horizontal = "center", vertical = "center")
#         ws['F3'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws['F3'].fill = PatternFill(start_color = '66CFCC', end_color = '66CFCC', fill_type = "solid")
#         ws['F3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['F3'] = 'CANT'

#         ws['G3'].alignment = Alignment(horizontal = "center", vertical = "center")
#         ws['G3'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws['G3'].fill = PatternFill(start_color = '66CFCC', end_color = '66CFCC', fill_type = "solid")
#         ws['G3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['G3'] = 'ESTATUS'

#         ws['H3'].alignment = Alignment(horizontal = "center", vertical = "center")
#         ws['H3'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws['H3'].fill = PatternFill(start_color = '66CFCC', end_color = '66CFCC', fill_type = "solid")
#         ws['H3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['H3'] = 'FECHA'

#         cont = 7

#         for datos in query:
#             ws.cell(row=cont, column=2).value= datos.nombre
#             ws.cell(row=cont, column=3).value= datos.ciclo
#             ws.cell(row=cont, column=4).value= datos.materia
#             ws.cell(row=cont, column=5).value= datos.calif
#             ws.cell(row=cont, column=6).value= datos.cant
#             ws.cell(row=cont, column=7).value= datos.estatus
#             ws.cell(row=cont, column=8).value= datos.fecha
#             cont+=1



#         #Establecer el nombre de mi archivo
#         nombre_archivo = "ReporteExcel.xlsx"
#         #Definir el tipo de respuesta que se va a dar
#         response = HttpResponse(content_type = "application/ms-excel")
#         contenido = "attachment; filename = {0}".format(nombre_archivo)
#         response["Content-Disposition"] = contenido
#         wb.save(response)
#         return response

#@login_required(login_url="login")
# def home(request):
#     #  directorio = request.GET.get('carpeta')
#     #  ruta = 
    
#     #  contenido = os.listdir(ruta)
#     #  csv = []
#     #  for fichero in contenido:
#     #      if os.path.isfile(os.path.join(ruta, fichero)) and fichero.endswith('.csv'):
#     #         csv.append(fichero) 
#     #         #print(imagenes)
    
#     #  for archivo in csv:
#     #     with open(archivo,"r") as archivo:
#     #         print(archivo.read())
    
#     if request.method == 'GET':
#         return render(request,'index.html', {'form': Directorio()})
#     else:
#         # ruta=request.POST.get('carpeta') #Retorna la ruta del archivo
#         # print(ruta)
#         # ruta_zip = "/home/angel/Escritorio/prueba.zip"
#         # archivo_zip = zipfile.ZipFile(ruta_zip, "r")
#         #archivo_zip = zipfile.ZipFile(request.POST.get('carpeta'))
        
#         print(request.FILES)
#         file_objs = request.POST.get('carpeta')
#         for file_obj in file_objs:
#             path = default_storage.save(settings.MEDIA_ROOT, ContentFile(file_obj.read()))
#             print("images path are",path)
#             # ruta_zip = "/home/angel/Escritorio/prueba.zip"
#             # archivo_zip = zipfile.ZipFile(ruta_zip, "r")
#             # print(archivo_zip.namelist())
#             # archivo_zip.close()
#             #archivo_zip.extractall(pwd=password, pat)
        
#         # archivo_zip.close()
#         return render(request,'index.html', {'form': Directorio()})


def login_view(request):
    return render(request,'paginas/login.html')