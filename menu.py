"""
Calculadora Cientifica Graficadora.
Modulo principal de interaccion por consola.
"""
import operaciones_basicas as basicas
import operaciones_cientificas as cientificas
import graficadora as graf
import historial as hist
historial = []# Lista donde se guardan las operaciones realizadas en la sesion


def ejecutar_operaciones_basicas() -> None: # Muestra el submenu de operaciones basicas y ejecuta la opcion elegida
    print("\nOperaciones basicas")
    print("-" * 40)
    print(" 1 - Suma")
    print(" 2 - Resta")
    print(" 3 - Multiplicacion")
    print(" 4 - Division")
    print(" 5 - Potencia")
    print(" 6 - Volver al menu principal")

    opcion = input("Ingrese la opcion: ")

    if opcion == "6":
        return

    if opcion in ["1", "2", "3", "4"]:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))

        if opcion == "1":
            resultado = basicas.sumar(a, b)
            operacion = "Suma: " + str(a) + " + " + str(b) + " = " + str(resultado)

        elif opcion == "2":
            resultado = basicas.restar(a, b)
            operacion = "Resta: " + str(a) + " - " + str(b) + " = " + str(resultado)

        elif opcion == "3":
            resultado = basicas.multiplicar(a, b)
            operacion = "Multiplicacion: " + str(a) + " * " + str(b) + " = " + str(resultado)

        elif opcion == "4":
            resultado = basicas.dividir(a, b)
            if resultado is None:
                print("Error: no se puede dividir entre cero.")
                return
            operacion = "Division: " + str(a) + " / " + str(b) + " = " + str(resultado)

        print("Resultado: " + str(resultado))
        hist.agregar_al_historial(historial, operacion)

    elif opcion == "5":
        base = float