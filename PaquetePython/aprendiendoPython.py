#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

#Primeros ejemplos de declaraciones de variables.
mi_variable = 46561321351
mi_cadena = "Hola me llamo Jesús"
mi_booleano = True
#Declaración de una costante.
MI_COSTANTE = 14

print mi_variable, mi_cadena, mi_booleano, MI_COSTANTE

#Ejemplo con operadores.
a = 5
b = 6
c = 45
mediaArit = (a + b + c)/3
print mediaArit

#Tipos de datos importantes en python.

mi_tupla = ('cadena de texto', 546654, True, 'otra cadena.')
print mi_tupla
print mi_tupla[0] #Pintamos el primer elemento de la tupla.
print mi_tupla[1] #Pintamos el segundo elemento de la tupla.
print mi_tupla[2] #Pintamos el tercer elemento de la tupla.
print mi_tupla[0:3] #Pintamos una porcion de la tupla.
print mi_tupla[:2]
print mi_tupla[2:]

#Listas, similar a una tupla, lo unico qu esta permite modificar los datos una vez creada, la tupla no.
mi_lista = ['Jesús ELvira Saánchez', 5465, 36.325, False ]
mi_lista[3] = True #Cambiamos el valor de la lista que se encuentra en el indice 3.

#Diccionarios, igual que las listas pero usan claves para declarar y acceder a los valores.
mi_diccionario = {'numero':3, 'nombre': "Jesús", 'apellido': "Elvira"}
print mi_diccionario['apellido']
#los diccionarios permiten borrar cualquier entrada.
#Tambien se pude cambiar el valor de sus elementos como en las listas.
mi_diccionario['apellido'] = "Sánchez"
print mi_diccionario['apellido']
del(mi_diccionario['numero']) #Operación de borrado de un elemento de el diccionario.

#Las listas se puden recorrer como matrices en java.
for i in mi_lista:
    print i
