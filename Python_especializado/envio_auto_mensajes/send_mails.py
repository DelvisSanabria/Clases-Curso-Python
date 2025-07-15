from smtplib import SMTP

from email.message import EmailMessage

#Probando el envio de mensajes via correo electronico

def sendEmail(to, subject, body, archive=None):
  #Configuro mi servidor
  smtp_server = "smtp.gmail.com"
  
  #Configuro mis puertos a usar
  smtp_ports = 587 or 465
  
  #Configuro el correo que usare como sender
  sender_Email = "delvissivira9@gmail.com"
  
  #Configuro la contraseña de aplicacion que usara para acceder a mi correo
  sender_key = 'sxrj dkif utzz umvc'
  
  #Maquetar nuestro mensaje
  
  email_mesage = EmailMessage() 
  
  #Configurar nuestro mensaje
  
  email_mesage["From"] = sender_Email
  email_mesage["To"] = to
  email_mesage["Subject"] = subject
  email_mesage.set_content(body)
  
  try:
    with open(archive, "rb") as arch:
      content = arch.read()
      email_mesage.add_attachment(content, maintype="application",subtype="octet-stream",filename=archive)
      print("archivo cargado correctamente")
  except Exception as e:
    print(f"Error al cargar el archivo adjunto: {e}")
    
  #Necesitamos conectarnos al servidor SMTP y enviar el mensaje
  
  with SMTP(smtp_server, smtp_ports) as servidor:
    #Creamos la capa de seguridad encriptada
    servidor.starttls()
    
    #Nos conectamos a el correo que enviara los mensajes
    servidor.login(sender_Email,sender_key)
    
    #Enviar finalmente nuestro correo electronico
    servidor.send_message(email_mesage)
  print("¡El correo se envio exitosamente!")
  
to = input("Ingrese el correo del destinatario: ")
subject = input("Ingrese el asunto del correo: ")
body = input("Ingrese el cuerpo del correo: ")

send_arch = input("¿Deseas enviar un archivo adjunto? (S/N)")
if send_arch.lower() == "s" or send_arch.lower() == "si":
  archive = input("Ingrese la ruta del archivo a adjuntar:")
else: 
  archive = None

print("Enviando correo, por favor espere...")

#Enviamos nuestro correo
sendEmail(to,subject,body,archive)