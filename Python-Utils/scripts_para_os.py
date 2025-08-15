import os
import shutil

#Crear un clasificador de archivos

#Para ordenar los archivos en carpeta su tipo (PDF, Excels,Imagenes, Ejecutables)


#Carpeta a organizar
Directory = "C:\\Users\\indatech\\Downloads"

#Categorias en que voy a organizar

categories = {
  "Documentos": [".pdf",".docx", "txt", ".xlsx"],
  "Imagenes": [".jpg", ".png", ".gif"],
  "Ejecutables": [".exe", ".msi", ".bat"],
  "Videos": [".mp4", ".mkv", "mov"],
  "Musica": [".mp3", ".wav"],
  "Otros": []
}

#Crear las carpetas si no existen

for category in categories:
  directory_route = os.path.join(Directory, category)
  if not os.path.exists(directory_route):
    os.mkdir(directory_route)
    
#Recorremos los archivos y los clasificamos

for archive in os.listdir(Directory):
  #ignorar carpetas
  if os.path.isfile(os.path.join(Directory, archive)):
    #necesitamos obtener el nombre y la extension
    name, extension = os.path.splitext(archive)
    extension = extension.lower()
    #Buscar las categorias
    for category, extensions in categories.items():
      if extension in extensions:
        #si la extension esta entre las extensiones que acepta una categoria movemos el archivo
        #a la carpeta de esa categoria
        origin = os.path.join(Directory, archive)
        destiny = os.path.join(Directory, category, archive)
        shutil.move(origin, destiny)
        break
    
      
#Extensión del Proyecto(De querer practicar)

""" 

- Borrar carpetas vacías: Usa os.rmdir() después de clasificar.
- Ordenar por fecha: Usa os.path.getmtime() para obtener fecha de modificación. 
-Manejar la logica de que si no encaja en ninguna categoria entre a la carpeta otros

"""