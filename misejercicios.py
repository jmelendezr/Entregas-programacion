##1ero
n1 = int(input("¿Cuántos elementos tiene la lista? "))

lista1 = [None] * n1  

for i in range(n1):
    lista1[i] = input("Ingresa un elemento: ")

conteo = {}
for elemento in lista1:
    conteo[elemento] = conteo.get(elemento, 0) + 1

elementos_unicos = [elemento for elemento, cantidad in conteo.items() if cantidad == 1]

if elementos_unicos:
    print("Elementos únicos en la lista:", elementos_unicos)
else:
    print("No hay elementos únicos en la lista.")

##2do
def palindromo(cadena):
    return cadena == cadena[::-1]

n2 = int(input("¿Cuántos elementos tendrá la lista? "))

lista2 = [None] * n2  
for i in range(n2):
    lista2[i] = input("Ingresa un elemento: ")

palindromos = [palabra for palabra in lista2 if palindromo(palabra)]

if palindromos:
    palindromo_mas_largo = max(palindromos, key=len)
    print(f"El palíndromo más largo es: {palindromo_mas_largo}")
else:
    print("No se encontraron palíndromos.")

##3ro
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales)

n3 = int(input("¿Cuántos elementos tiene la lista? "))

lista3 = [None] * n3  
for i in range(n3):
    lista3[i] = input("Ingresa un elemento: ")

# Buscar la palabra con más vocales
if lista3:
    palabra_mas = max(lista3, key=contar_vocales)
    cantidad_vocales = contar_vocales(palabra_mas)
    print(f"La palabra con más vocales es: '{palabra_mas}' con {cantidad_vocales} vocales.")
else:
    print("La lista está vacía.")

##4to
def es_palindromo(lista4):
    return lista4 == lista4[::-1]

n = int(input("¿Cuántos elementos tiene la lista? "))

lista4 = [None] * n  
for i in range(n):
    lista4[i] = input("Ingresa un número: ")

if es_palindromo(lista4):
    print(f"La lista {lista4} es un palíndromo.")
else:
    print(f"La lista {lista4} no es un palíndromo.")

