"""
Ejercisio.3
Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.
"""

n = int(input("N = "))

total_nomina=0.0

for s in range(n):
    sueldo=float(input("Ingrese el sueldo:"))
    total_nomina = total_nomina + sueldo


print("Nomina:", total_nomina)

