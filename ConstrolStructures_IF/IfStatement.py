#Bloque 1: Statement if
"""
print("Esto es una asignación: ", "x=1")
print("Esto es una comparación: ", "x==1")
#Este es el Ejemplo 1:
num = int(input('Enter a number: '))
if num < 0:
 print(num, 'is negative')
"""

#Bloque 2: Indentaciones
"""
num = int(input('Enter another number: '))
if num > 0:
	print(num, 'is positive')
	print(num, 'squared is ', num * num)
print('Bye')
"""
#Bloque 3: El caso else
"""
num = int(input('Enter yet another number: '))
if num < 0:
    print('Its negative')
else:
    print('Its not negative')
print('Bye')
"""
#Bloque 4: El caso elif

savings = float(input("Enter how much you have in savings: "))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print('Well done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome Sir!')
else:
    print('Thank you')
    

#Bloque 5: Anidamiento
"""
snowing = True
temp = -1
if temp < 0:
 print('It is freezing')
 if snowing:
  print('Put on boots')
  print('Time for Hot Chocolate')
print('Bye')
"""
#If simple
"""
age = 15
status = None
if (age > 12) and age < 20:
    status = 'teenager'
else:
    status = 'not teenager'
print(status)
"""
#If con expresiones
"""
age = 15
status = None
status = ('teenager'if age > 12 and age < 20 else 'not teenager')
print(status)
"""
#Prácticas I
"""
##
#Determinar y mostrar cuando un número entero introducido por el usuario es par o no.
#

#Leer el entero desde el usuario
num = int(input("Entre un entero: "  ))
#Determinando cuando es none o par usando
#el operador de módulo (resto)

if num % 2 == 1:
	print(num, "is odd. " )
else:
	print(num, "is even")
print("Bye")
"""
"""
#Práctica II
#
## Determinar si la letra es vocal o consonante
#
#Leer una letra desde el usuario
letter = input("Entra  una letra desde el usuario:  " )

#Clasificar la letra y  reportar el resultado

if letter == " a " or  letter == " e "  or  \
    letter == " i " or  letter == " o "  or  \
    letter == " u " :
    print("It´s a vowel. ")
elif letter == "y":
	print("i Sometime it`s a vowel…Sometimes it`s a consonant. " )
else:
	print( "It`s a consonant")

"""