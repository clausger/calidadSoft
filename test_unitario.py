import pytest
from calculadora import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5

def test_division_por_cero():
    calc = Calculadora()
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10, 0)
