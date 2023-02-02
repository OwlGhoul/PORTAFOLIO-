# -*- coding: utf-8 -*-
"""01 variables.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YwoS-EXmxsjP7ix-zL9hZwjeSh5qZrk1

Variables
"""

name = "Pedro jesus"
user_id = 92220117
progress =  0.00
exp = 10
verified = True #bool / booleano

"""El valor de una variable se puede reasignar. sin embargo recordemos que siempre tomara como valor definitivo el ultimo en asignarle"""

xp = True
xp = False

print(xp)

"""# **Data** **Types**

# int
El tipo de dato **integer** o **entero** hace referencia a un valor numerico, dicho valor no permite almacenar numeros decimales sin embargo nos permite alojar numeros positivos y negativos
"""

Year = 2023
age = 27

"""# Float
El dato **flotante** o **punto flotante** es aquel que hace referencia a un valor numerico el cual Si permite numeros decimales
"""

pi =3.141592
apple_cost = 12.99

"""# String
Los **strings** o **cadenas** es un tipo de dato que nos permite alojar textos, estos se deben de poner siempre entre comillas ya sean dobles "" o comillas simples ''
"""

message = "saludos a todos"
user = '@ErickBorges'

"""# Boolean
Los booleanos almacenan valores que pueden ser unicamente **verdaderos** o **falsos**. En python escribimos con mayuscula la inicial de valor.
"""

approved = False
late_to_class = True

"""# Comments

"""

# Esto es un comentario en nuestro codigo.
print("Hola mundo")
"""
Esre es un comentario de varias lineas
se pone usando tres pares  de comillas dobles
o comillas simples
"""

"""# Concatenacion

"""

print(name, age, verified)
print("este es un texto: ", verified)

"""## Imprimir el tipo de dato"""

print(type("hola mundo"))
print(type(5))
print(type(1.5))
print(type(True))
print(type(3 + 1))
print(type([1, 2, 3]))
print(type({name: 'erick'}))

"""# Variables en una sola linea"""

name, surname, alias, age = "erick", "borges", "Alecs", 23
print("me llamo:", name, surname)
print("mi edad es", age,", mis amigos me dicen:", alias)

"""# Asignar valor a variables por el usuario"""

first_name = (input('¿como te llamas '))
age = input('cuantos años tienes?')

print(first_name, age)

"""# Funciones del sistema
print() = imprime en pantalla

type() = nos da el tipo de dato a trabajar

len() = nos dice el tipo de dato

str = la cantidad de caracteres
"""

print(len(name))

my_int_variable = 4
print(my_int_variable)
print(type(my_int_variable))

new_variable = str(my_int_variable)
print(new_variable)
print(type(new_variable))