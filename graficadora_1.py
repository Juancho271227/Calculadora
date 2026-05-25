"""
Calculadora Cientifica Graficadora.
Modulo de graficacion en consola.
"""

# Diccionario con las funciones disponibles y su descripcion
funciones = {
    "lineal": "f(x) = 2x + 1",
    "cuadratica": "f(x) = x^2",
    "cubica": "f(x) = x^3"
}


def calcular_funcion(nombre_funcion: str, x: float) -> float:
    # Evalua la funcion en el valor x y retorna el resultado
    # Retorna None si la funcion no existe
    if nombre_funcion == "lineal":
        return 2 * x + 1
    elif nombre_funcion == "cuadratica":
        return x * x
    elif nombre_funcion == "cubica":
        return x * x * x
    return None


def graficar_funcion(nombre_funcion: str, x_inicio: float, x_fin: float,
                     pasos: int) -> None:
    # Grafica una funcion en consola usando el caracter *
    # Cada fila es un valor de x y la posicion del * representa el valor de y
    if nombre_funcion not in funciones:
        print("La funcion '" + nombre_funcion + "' no esta disponible.")
        print("Funciones disponibles: lineal, cuadratica, cubica")
        return

    if pasos <= 1:
        pasos = 2

    incremento = (x_fin - x_inicio) / (pasos - 1)
    ancho = 40

    # Calcular todos los valores de y y guardarlos en una lista
    valores_y = []
    x_actual = x_inicio
    for i in range(pasos):
        y = calcular_funcion(nombre_funcion, x_actual)
        valores_y.append(y)
        x_actual = x_actual + incremento

    # Buscar el minimo y el maximo valor de y para escalar la grafica
    y_min = valores_y[0]
    y_max = valores_y[0]
    for y in valores_y:
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y

    print("\nGrafica de la funcion: " + nombre_funcion)
    print("Rango x: [" + str(x_inicio) + ", " + str(x_fin) + "]")
    print("-" * (ancho + 2))

    for y in valores_y:
        if y_max == y_min:
            posicion = 0
        else:
            posicion = int((y - y_min) / (y_max - y_min) * (ancho - 1))

        linea = " " * posicion + "*"
        print(linea)

    print("-" * (ancho + 2))