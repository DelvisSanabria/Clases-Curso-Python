import os 
import glob

def clean_temp_files():
  """ Defino la ruta de los archivos temporales del sistema """
  temp_dirs = [
    "C:/Windows/Temp/*",
    os.path.expanduser("~\\AppData\\Local\\Temp\\*")
  ]
  
  #ejecuto mi bucle para limpiar
  
  for temp_dir in temp_dirs:
    for archive in glob.glob(temp_dir):
      try:
        if os.path.isfile(archive):
          os.remove(archive)
          print(f"Eliminado: {archive}")
      except Exception as e:
        print(f"Error eliminando: {archive}: {str(e)}")

if __name__ == "__main__":
  clean_temp_files()