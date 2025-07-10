def sum(a,b):
  return a + b

def rest(a,b):
  return a - b

def multiply(a,b):
  return a * b


def divide(a,b):
  if b == 0:
    #raise lanza una excepcion del tipo que nosotros definamos con un mesaje que nosotros definimos
    raise ValueError("No se puede dividir por 0")
  return a / b