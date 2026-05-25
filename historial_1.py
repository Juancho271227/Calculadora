"""
Calculadora Cientifica Graficadora.
Modulo de historial de operaciones.
"""


def agregar_al_historial(historial: list, operacion: str) -> None: # Agrega la operacion realizada al final del historial
    historial.append(operacion)


def mostrar_historial(historial: list) -> None: # Muestra todas las operaciones guardadas en el historial
    print("\nHistorial de operaciones")
    print("-" * 40)

    if len(historial) == 0:
        print("El historial esta vacio.")
    else:
        for i in range(len(historial)):
            print(str(i + 1) + ". " + historial[i])

    print("-" * 40)


def limpiar_historial(historial: list) -> None: # Elimina todas las operaciones del historial
    historial.clear()
