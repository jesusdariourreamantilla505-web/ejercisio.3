"""
Ejercisio.5
Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada
una. Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo.
"""
n = int(input("N = "))

grupo1 = 0
grupo2 = 0
grupo3 = 0

for i in range(n):
    venta = float(input("Ingrese el valor de la venta: "))
    
    if venta <= 200:
        grupo1 = grupo1 + 1
    elif venta < 400:
        grupo2 = grupo2 + 1
    else:
        grupo3 = grupo3 + 1


print("Grupos 1, 2 y 3:", grupo1, ";", grupo2, ";", grupo3)