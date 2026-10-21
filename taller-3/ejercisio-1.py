"""
Ejercisio.1
Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.

"""
A=int(input("Ingrese el numero 1:"))
B=int(input("Ingrese el numero 2:"))


if A <= B:
    paso=1
elif A > B:
    paso=-1

print(list(range(A, B + 1,paso)))