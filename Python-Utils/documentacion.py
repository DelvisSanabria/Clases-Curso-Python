""" 
documentacion.py - modulo para explicar documentacion

Funcionalidades:
  1. documentacion estilo Docstrings (comillas triples)
  2. Google Style

Autor: Delvis Sanabria
Version: 1.2.0
"""

#La documentacion es la descripcion estructurada de: 
""" 
Proposito del codigo

funcionalidades implementadas

Interfaces y parametros

ejemplos de uso 

Dependencias y requisitos

"""

#1.documentacion estilo Docstrings (comillas triples)

def calculate_iva(mount, percentage=16):
  """ 
  Calcula el iva de un monto dado.
  
  Args:
      mount (float): Cantidad base para el calculo
      percentage (int, optional): Porcentaje de IVA. Defaults to 16.
  Returns:
      float: Valor del IVA calculado
  Examples:
      >>> calculate_iva(100)
      16.0
  """
  return mount * (percentage / 100)

#2. Google Style:

def sum_example(param1,param2):
  """
    Descripcion breve: Funcion que suma dos parametros
  
    Descripcion extendida: esta funcion toma dos parametros variables para
    sumarlos directamente en el retorno
  
    Args:
      param1 (int): Primer parametro a sumar
      param2 (int): Segundo parametro a sumar
    Returns:
      int: Resultado de la suma de los parametros
    Examples:
      >>> sum_example(1,2)
      3
  """
  return param1 + param2

def multiply(param1, param2):
  """
    Funcion que multiplica dos parametros
  
    Esta funcion toma dos parametros variables para
    multiplicarlos directamente en el retorno
  
    Args:
      param1 (int): Primer parametro a multiplicar
      param2 (int): Segundo parametro a multiplicar
    Returns:
      int: Resultado de la multiplicacion de los parametros
    Examples:
      >>> multiply(2,3)
      6
  """

  return param1 * param2