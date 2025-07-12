#Pywhatkit Es una libreria para enviar mensajes de texto a traves de whatsapp
import pywhatkit as ws

#Enviar mensaje de forma instantanea, el metodo sendwhatmsg_instantly recibe como parametros el numero de telefono, el mensaje y el tiempo de envio, el tiempo de envio es en segundos

ws.sendwhatmsg_instantly("+584126794556","Mensaje de prueba")

#Forma agendada de envio de mensajes a un numero

ws.sendwhatmsg("+584126794556","Mensaje de prueba",21,3)

#Enviar mensajes instantaneos a un grupo en especifico 

#Link al grupo de python: https://chat.whatsapp.com/GjtWD6Qc9Td1KJTJZnz7MZ

ws.sendwhatmsg_to_group_instantly("GjtWD6Qc9Td1KJTJZnz7MZ","Hola estamos practicando envio automatico de mensajes")

#Forma agendada de envio de mensajes a un grupo

ws.sendwhatmsg_to_group("GjtWD6Qc9Td1KJTJZnz7MZ","Hola estamos practicando envio automatico de mensajes",21,6)

#Puedo enviar imagenes y videos

ws.sendwhats_image("GjtWD6Qc9Td1KJTJZnz7MZ","./Python_especializado/envio_auto_mensajes/descarga.jpg", "Imagen enviada de prueba")

#les podria llegar a dar un error como este:

#ModuleNotFoundError: No module named 'win32clipboard'

#se soluciona instalando la siguiente libreria:

#pip install pywin32


number_list = ["+584126794556","+584126794556","+584126794556","+584126794556"]

for number in number_list:
  ws.sendwhatmsg_instantly(number,"Mensaje de prueba en un bucle")
  
#menu interactivo de envio de mensajes e imagenes

def sendMsg():
  number = input("Ingresa tu numero telefonico, en formato internacional")
  msg = input("Ingresa el mensaje que quieres enviar")
  ws.sendwhatmsg_instantly(number,msg)
  
#crear metodo para enviar, mensaje a grupo, imagen a persona, imagen a grupo, y enviar mensaje agendado