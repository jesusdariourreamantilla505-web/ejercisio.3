"""
Ejercisio.6
Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.

"""
n = int(input("N = "))

ganador_id = 0
menor_tiempo = 0.0

# PROCESO Y SALIDA
for i in range(n):
    print("Datos del ciclista", i + 1)
    identificador = int(input("Identificador: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    centesimas = int(input("Centésimas: "))

    # Fórmulas dadas en la guía
    tiempo = (60 * minutos) + segundos + (centesimas / 100)[span_7](start_span)[span_7](end_span)
    velocidad = 900 / tiempo[span_8](start_span)[span_8](end_span)

    # Imprimimos la velocidad del ciclista actual
    print("Ciclista", identificador, "velocidad:", velocidad, "km/h")

    # Evaluamos quién tiene el menor tiempo para elegir al ganador
    if i == 0 or tiempo < menor_tiempo:
        menor_tiempo = tiempo
        ganador_id = identificador


print("Ganador:", ganador_id)
