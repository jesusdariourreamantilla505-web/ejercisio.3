"""
Ejercisio.7
Se reciben N empleados, con 1 ≤ N ≤ 40. Cada registro contiene, en este orden,
identificador entero positivo único, edad entera no negativa en años y años enteros de
antigüedad entre 1 y 50. El sueldo ficticio es la suma de una base de 100 unidades monetarias,
el valor numérico de la edad y la suma de los enteros desde 1 hasta la antigüedad; toda esa
suma se divide entre los años de antigüedad. La edad y la suma de años se consideran aportes
numéricos en unidades monetarias dentro de este modelo ficticio. Informe el sueldo de cada
empleado, el total de la nómina y los identificadores con mayor y menor sueldo. En empate
conserve el primero recibido.

"""

n = int(input("N = "))

total_nomina = 0.0
mayor_sueldo = 0.0
menor_sueldo = 0.0
mayor_id = 0
menor_id = 0

for i in range(n):
    print("Datos del empleado", i + 1)
    identificador = int(input("Identificador: "))
    edad = int(input("Edad: "))
    antiguedad = int(input("Antigüedad: "))

    
    suma_antiguedad = 0
    for j in range(1, antiguedad + 1):
        suma_antiguedad = suma_antiguedad + j

    
    sueldo = (100 + edad + suma_antiguedad) / antiguedad

    
    print("Empleado", identificador, "sueldo:", sueldo)

    
    total_nomina = total_nomina + sueldo

    
    if i == 0:
        mayor_sueldo = sueldo
        mayor_id = identificador
        menor_sueldo = sueldo
        menor_id = identificador
    else:
        if sueldo > mayor_sueldo:
            mayor_sueldo = sueldo
            mayor_id = identificador
        if sueldo < menor_sueldo:
            menor_sueldo = sueldo
            menor_id = identificador

#
print("Nómina:", total_nomina)
print("Mayor:", mayor_id)
print("Menor:", menor_id)
