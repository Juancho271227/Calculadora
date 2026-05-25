"""
Calculadora Cientifica Graficadora.
Modulo de operaciones basicas.
"""


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:

    return a * b


def dividir(a: float, b: float) -> float:
    """Calcula la division de dos numeros.
       Si el divisor es cero retorna None.
    """
    if b == 0:
        return None
    return a / b


def potencia(base: float, exponente: int) -> float:
    """Calcula la potencia de una base elevada a un exponente entero.
       Implementado mediante multiplicaciones sucesivas.
       Si el exponente es negativo se calcula el inverso del resultado.
    """
    resultado = 1
    exponente_abs = exponente

    if exponente < 0:
        exponente_abs = -exponente

    for i in range(exponente_abs):
        resultado = resultado * base

    if exponente < 0:
        return 1 / resultado

    return resultado
