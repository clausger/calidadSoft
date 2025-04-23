class Calculadora:
    def sumar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b
