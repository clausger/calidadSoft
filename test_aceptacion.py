from calculadora import Calculadora

def test_flujo_completo_usuario():
    calc = Calculadora()
    
    # Escenario 1: El usuario suma dos números
    resultado_suma = calc.sumar(10, 20)
    assert resultado_suma == 30, "La suma debería ser 30"

    # Escenario 2: El usuario divide el resultado anterior
    resultado_division = calc.dividir(resultado_suma, 5)
    assert resultado_division == 6, "El resultado final debería ser 6"
