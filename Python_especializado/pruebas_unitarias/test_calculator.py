#Las pruebas unitarias son un conjunto de pruebas que se realizan para verificar la calidad de un software.

#Pytest es una herramienta para realizar pruebas unitarias en Python

#Nuestros de test deben de ajuro, por que si, siempre comenzar con test_ o terminar 

from calculator import sum, rest, multiply, divide
import pytest

#Test para las funciones de calculator
def test_sum():
  assert sum(1,2) == 3
  
def test_rest():
  assert rest(1,2) == -1
  
def test_multiply():
  assert multiply(1,2) == 2
  
def test_divide():
  assert divide(1,2) == 0.5
  
def test_divide_by_zero():
  with pytest.raises(ValueError):
    divide(1,0)
