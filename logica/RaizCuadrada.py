import math

class RaizCuadrada:
    def calcular_raiz_cuadrada(numero):
        if numero < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo"
        else:
            return math.sqrt(numero)