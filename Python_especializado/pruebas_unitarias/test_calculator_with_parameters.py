#Las pruebas unitarias parametrizadas, son pruebas las cuales pueden recibir multiples valores

from calculator import sum, rest, multiply, divide
import pytest

@pytest.mark.parametrize("num1, num2, expected_result", [
  (1,1,2), #Test case 1
  (-2,-3,-5), #Test case 2
  (3,0,3), #Test case 3
  (4,4,8), #Test case 4
  (-15,5,-10) #Test case 5
])

#Test para las funciones de calculator
def test_sum(num1,num2, expected_result):
  assert sum(num1,num2) == expected_result
  
@pytest.mark.parametrize("num1, num2, expected_result", [
  (1,1,0), #Test case 1
  (-2,-3,1), #Test case 2
  (3,0,3), #Test case 3
  (4,4,0), #Test case 4
])

def test_rest(num1,num2, expected_result):
  assert rest(num1,num2) == expected_result
  
#tarea generar las pruebas parametrizadas para la multiplicacion
def test_multiply():
  assert multiply(1,2) == 2
  
@pytest.mark.parametrize("num1, num2, expected_result, raise_error", [
  (10,2, 5.0, False), #Test case 1
  (7,2,3.5, False), #Test case 2
  (10,0,None, True), #Test case 3
])
  
def test_divide(num1,num2, expected_result, raise_error):
  if raise_error:
    with pytest.raises(ValueError):
      divide(num1,num2)
  else:
    assert divide(num1,num2) == expected_result
