"""
Ejercisio.2
Se conoce el primer término A, la diferencia D y la cantidad N de términos de una
progresión. A y D son enteros entre -100 y 100, y N está entre 0 y 1000. Determine la suma de
los N términos; si N es cero, el total es cero.
"""
A=int(input("Ingrese A:"))
D=int(input("Ingrese D:"))
N=int(input("Ingrese N:"))

t = A
s = 0
for k in range(1, A+1):
    s = s + t
    t = + D

print(s)

# s=0, 1 2 3 4 5 = 15, s1=1, s2=3, s4=10, s5= 15
# s=0, 3
