from PIL import Image
import os

def convert_img(destiny_format=".jpg", quality=80):
  "Crea mis formatos soportados y mi directorio"
  support_format=[".jpeg", ".png", ",webp"]
  directory= "C:\\Users\\indatech\\Downloads"
  
  for archive in os.listdir(directory):
    name, extension = os.path.splitext(archive)
    
    if extension.lower() in support_format:
      try:
        img = Image.open(os.path.join(directory, archive))
        new_rute = os.path.join(directory, f"{name}.{destiny_format}")
        
        img.save(new_rute, destiny_format, quality=quality)
        print(f"Convertido: {archive} a {name}.{destiny_format}")
      except Exception as e:
        print(f"Error convirtiendo {archive}:{str(e)}")
if __name__ == "__main__":
  convert_img()