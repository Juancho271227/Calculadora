"""
Calculadora Cientifica Graficadora.
Modulo de operaciones cientificas.
"""


def factorial(n: int) -> int: # Calcula el factorial de n
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado


def raiz_cuadrada(x: float, iteraciones: int = 20) -> float:
    # Aproxima la raiz cuadrada usando el metodo de Newton-Raphson
    # Retorna None si x es negativo
    if x < 0:
        return None
    if x == 0:
        return 0

    aproximacion = x / 2
    for i in range(iteraciones):
        aproximacion = (aproximacion + x / aproximacion) / 2

    return aproximacion


def exponencial(x: float, terminos: int = 20) -> float: # Aproxima e^x usando la serie de Taylor
    resultado = 0
    for k in range(terminos):
        potencia_x = 1
        for j in range(k):
            potencia_x = potencia_x * x
        resultado = resultado + potencia_x / factorial(k)
    return resultado


def seno(x: float, terminos: int = 15) -> float: # Aproxima el seno de x en radianes usando la serie de Taylor
    resultado = 0
    for k in range(terminos):
        exponente = 2 * k + 1

        potencia_x = 1
        for j in range(exponente):
            potencia_x = potencia_x * x  # Signo alternado: positivo en pares, negativo en impares
        if k % 2 == 0:
            resultado = resultado + potencia_x / factorial(exponente)
        else:
            resultado = resultado - potencia_x / factorial(exponente)

    return resultado


def coseno(x: float, terminos: int = 15) -> float:
    # Aproxima el coseno de x en radianes usando la serie de Taylor
    resultado = 0
    for k in range(terminos):
        exponente = 2 * k

        potencia_x = 1
        for j in range(exponente):
            potencia_x = potencia_x * x # Signo alternado: positivo en pares, negativo en impares
        if k % 2 == 0:
            resultado = resultado + potencia_x / factorial(exponente)
        else:
            resultado = resultado - potencia_x / factorial(exponente)

    return resultado


def logaritmo_natural(x: float, terminos: int = 100) -> float:
    # Aproxima ln(x) usando la formula: ln(x) = 2 * suma((u^(2k+1)) / (2k+1)) Retorna None si x es menor o igual a cero
    if x <= 0:
        return None

    u = (x - 1) / (x + 1)
    resultado = 0

    for k in range(terminos):
        exponente = 2 * k + 1

        potencia_u = 1
        for j in range(exponente):
            potencia_u = potencia_u * u

        resultado = resultado + potencia_u / exponente

    return 2 * resultado