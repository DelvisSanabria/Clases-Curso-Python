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

API_KEY = "tu_api_key"
city = "Madrid"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"