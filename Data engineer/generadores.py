texto = "el niño hace mucho dinero"
coleccion = texto.split()
"""resultado = []
for elemento in coleccion:
    if 'e' in elemento: 
        resultado.append(elemento)"""

#Convertir un bucle for existente que produce una lista en una comprensión de lista
colection = [elemento for elemento in coleccion if 'e' in elemento]
#print(colection)

# Crear una función generadora para producir la secuencia Fibonacci
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a 
        a , b = b, a+b

for num in fibonacci(9):
    print(num)

#Determinar si una secuencia incorporada en Python como una Cadena es un iterador o un iterable

#Imprimir los 5 primeros elementos de un generador sin guardar la secuencia completa
generador = (i for i in range(2,10))

for num in generador:
    print(num)
    if num > 5:
        break

#Escriba una comprensión de lista para filtrar los números impares de una lista

impares = [numero for numero in range (20) if numero %2 != 0]
print (impares)