#Cree una función que compruebe si una palabra es un palíndromo
import random, string
from datetime import datetime

def palindromo(word):
    word = word.lower()
    palindro = word[::-1]
    if word == palindro: 
        return True
    else: 
        return False
    
    
print(palindromo("radar"))

def mayor(numer1, number2, number3):
    return max(numer1, number2, number3)

#Desarrolle una función que formatee una cadena de fecha en un formato legible
def formatear_fecha(fecha):
    return fecha.strftime("%d/%m/%Y %H:%M:%S")

#Defina una función para generar una contraseña aleatoria
def contraseña_random():
    caracteres = string.ascii_letters + string.digits
    contraseña = ""
    for i in range(10):
        contraseña += "".join(random.choice(caracteres))
    return contraseña

print(contraseña_random())

print(mayor(5, 10, 3))
print(formatear_fecha(datetime.now()))
