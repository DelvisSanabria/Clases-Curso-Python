import requests

#obtener los datos de un pokemon

url = "https://pokeapi.co/api/v2/pokemon/pikachu" 

#creemos nuestra respuesta

response = requests.get(url)

#verifiquemos que la respuesta fue exitosa

if response.status_code == 200:
  data = response.json()
  print(f"Nombre: {data['name']}")
  print(f"Altura: {data['height']}")
  print(f"Habilidad: {data['abilities'][0]['ability']['name']}")
else:
  print(f"Error al obtener los datos del Pokémon: {response.status_code}")
  
  
#Opcional:Crearse una cuenta en OpenWeatherMap y obtener una API Key, para pintar los datos del clima de una ciudad.
  
  
#https://openweathermap.org/api

API_KEY = "83c6746c66c8f1e4161a00e50d680d25"
city = "Caracas"

Latitude= 10.4806

Longitude= 66.9036
url = f"https://api.openweathermap.org/data/2.5/weather?lat={Latitude}&lon={Longitude}&appid={API_KEY}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    climate = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    print(f"Clima en {city}: {climate}")
    print(f"Temperatura: {temp}°C")
else:
    print("Error al obtener datos.")