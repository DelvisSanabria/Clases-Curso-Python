from bs4 import BeautifulSoup
import requests
import os

#Vamos a leer un archivo local en modo solo lectura
with open("./Python-Backend/webScrapping/beautifulSoup/index.html", "r", encoding="utf-8") as html_file:
  """ Abro mi archivo y lo guardo en una variable """
  html = html_file.read()
  
soup = BeautifulSoup(html, "html.parser")

#Vamos a extraer los titulares
title = soup.find("h1")
""" title = soup.find("p", class_="text") """

#vamos a traernos todos los parrafos
paragraphs = soup.find_all("p")

#vamos a mostrar mi h1
print(title.text)


#vamos a mostrar todos los parrafos
for paragraph in paragraphs:
  print(paragraph.text)
  

url = "https://www.amazon.com/s?k=gaming"
second_url ="https://www.amazon.com/s?k=gaming&page=2"

#necesito configurar cabeceras
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36",
  "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.6,en;q=0.4"
}

#hacemos nuestra peticion 
""" response = requests.get(url, headers=headers) """
response = requests.get(second_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


#Buscamos todos los productos (Las clases pueden variar verifica)
products = soup.find_all("div", {"class": "s-card-container"})

""" print(products) """

print("\n")
print("Aqui comienza mi scrappin de productos")

save_directory = "downloaded_images"
os.makedirs(save_directory, exist_ok=True) 

for product in products:
  try:
    name = product.find("h2", {"class": "a-text-normal"}).text
    price = product.find("span", {"class": "a-offscreen"}).text
    
    """ Si fuera una imagen """
    image_url = product.find("img").get('src')
    
    """ Hago mi primera verificacion """
    if not image_url.startswith(("http", "https")):
      """ Le agrego el protocolo https a la imagen """
      image_url = "https:" + image_url
    
    """ Extraigo el nombre de la imagen """
    filename = os.path.basename(image_url)
    """ Si no lo tiene asigno un nombre """
    if not filename:
      filename = f"image-{hash(image_url)}.jpg"
      
    """ Creamos el directorio donde guardaremos la imagen y la guardamos vacia """
    filepath = os.path.join(save_directory, filename)
   
    """ Intentamos descargar la imagen """
    try:
      """ Intentamos descargar la imagen y su contenido """
      image_data = requests.get(image_url).content
      with open(filepath, "wb") as f:
        f.write(image_data)
    except Exception as e:
      print(f"Error al descargar la imagen: {e}")
    
    print(f"Producto: {name} Precio: {price}")
  except:
    pass
  
#Ejercicios opcionales
"Crear una base de datos para almacenar todos los valores y la url de cada producto"
"hacerle web scrapping a mercadolibre traerse titulos y precios"