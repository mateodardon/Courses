def calcular_promedio(numeros):
    suma = 0
    for n in numeros:
        suma += n
    promedio = suma / len(numeros)
    return promedio

def restar(numeros):
    resulatdo = numeros[0]
    for n in numeros[1:]:
    	resultado -= n
    return resulatdo

datos = [10, 20, 30, 40]
resultado = calcular_promedio(datos)
print(f"El promedio es: {resultado}")
