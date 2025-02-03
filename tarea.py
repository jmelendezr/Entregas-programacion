 ##1ero
n = int(input("¿Cuántos elementos tiene la lista? "))

lista = [None] * n  

for i in range(n):
    lista[i] = input("Ingresa un elemento: ")

if len(lista) == len(set(lista)):
    print("La lista no tiene elementos repetidos.")
else:
    print("La lista tiene elementos repetidos.")

##2do
def palindromo1(cadena):
    return cadena == cadena[::-1] 

n = int(input("¿Cuántos elementos tendrá la lista? "))


lista = [None] * n  
for i in range(n):
    lista[i] = input("Ingresa un elemento: ")

palindromos = [palabra for palabra in lista if palindromo1(palabra)]


if palindromos:
    print("Palíndromo encontrado:", palindromos[0])
else:
    print("NO EXISTE")
##3ro
def x(cadena): 
    vocales = "aeiouAEIOU"
    contador = sum(1 for letra in cadena if letra in vocales) 
    return contador >= 2

n = int(input("¿Cuántos elementos tiene la lista? "))

lista = [None] * n  
for i in range(n):
    lista[i] = input("Ingresa un elemento: ")

cadenas_vocales = [palabra for palabra in lista if x(palabra)]

if cadenas_vocales:
    print("Cadena encontrada:", cadenas_vocales[0])
else:
    print("No existe")
##4to
def x(lista):
    return lista == lista[::-1]

n = int(input("¿Cuántos elementos tiene la lista? "))

lista = [None] * n  
for i in range(n):
    lista[i] = input("Ingresa un elemento: ")

if x(lista):
    print("La lista es un palíndromo:", lista)
else:
    print("No es palindromo")