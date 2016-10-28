#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

#Estructuras de control y flujo.
#Asignación multiple, una de las ventajas de python, con una tupla tambien se puede hacer.
a, b , c = 'hola', 45, 125
print a, b ,c

#Estructura de control de flujo condicional
# operadores ==, !=, <, >, <=, >=
# operadores realcionales and, or xor
semaforo = "hola"
verde = "hola"
if semaforo == verde:
    print "puede cruzar."
    #añadir el código respetando la identación
else:
    print "No puede cruzar."
    #añadir el código respetando la identación

#ESTRUCTURAS DE COBTROL ITERATIVAS.

contador = 0

#While, tambien existe el break para salirse del bucle.
while contador < 10:
    contador += 1
    print contador

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for. se puden recorrer tuplas y listas.
for elemento in listaNumeros:
    print elemento

#Otras formas de usar el for muy utiles.
for numero in range(0,50):
    print numero
