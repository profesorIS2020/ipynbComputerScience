
##
# Trabajo con tuplas
#
# Crear una tupla con los nombres de los meses
months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
          "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", 
          "Diciembre")
l1 = list(months)  # Convertir la tupla a una lista
months = tuple(l1)  # Cambiar el primer mes a "January" 
print(months)# Mostrar la tupla

# Acceso a los miembros de la tupla:
print("El primer mes es", months[0])
print("El segundo mes es", months[1])  
print("El último mes es", months[-1])






## 
# Mostrar enteros a partir de entrada de usuario y en orden ascendente
# 

# Comenzar con una lista vacía
data = []

# Leer valores, adicionarlos a la lista hasta que el usuario entre 0

num = int(input("Entre un entero (0 para salir): "))
while num != 0:
	data.append(num)
	num = int(input("Entre un entero (0 para salir): "))

# Ordene los valores

# Mostrar los valores en orden ascendente

print("Los valores, ordenados en orden ascendente, son: ")

for num in data:
	print(num)


##
# Eliminar los valores atípicos de un set de datos
# 

## Eliminar los valores atípicos de una lista de datos 
# @param list los valores a procesar
# @param num_outliers el número más pequeño y mas grande a eliminar
#@return Devolver una nueva copia de los datos donde los valores son ordenados en orden ascendente yel valor más pequeño y el más grande han sido eliminados

def removeOutliers(list, num_outliers):
	# Crear una nueva copia de la lista ordenada
	retval = sorted(list)

	#Eliminar los valores atípicos más grandes
	for i in range(num_outliers):
		retval.pop()
	#Eliminar los valores atípicos más pequeños
	for i in range(num_outliers):
		retval.pop(0)
	#Retornar el resultado
	return retval
	
# Leer la data desde el usuario y eliminar los dos valores más grandes y los dos más pequeños

def main():
    # Lee los valores desde el usuario hasta que una línea en blanco es entrada.
    values = []
    s = input("Entra un valor (blanco para salir): ")
    while s != "":
        values.append(float(s))
        s = input("Entra un valor (blanco para salir): ")
    # Display el resultado o un mensaje de error apropiado
    if len(values) < 4:
        print("No puedes entrar muchos valores.")
    else:
        print("Los valores sin los valores atípicos son: ")
        for v in removeOutliers(values, 2):
            print(v)

# Llamar a la función principal si este archivo no ha sido importado
if __name__ == "__main__":
    main()

##
# Calcular la media y la desviación estándar de un set de datos
#
#
# Calcular la media y la desviación estándar de una lista de datos
# @param list los valores a procesar
# @return una tupla que contiene la media y la desviación estándar de los valores

def calculateStats(list):
    # Calcular la media
    sum = 0
    for num in list:
        sum += num
    mean = sum / len(list)
    
    # Calcular la desviación estándar
    sum_squares = 0
    for num in list:
        sum_squares += (num - mean) ** 2
    std_dev = (sum_squares / (len(list) - 1)) ** 0.5
    
    # Retornar los resultados
    return (mean, std_dev)

# Leer la data desde el usuario y mostrar la media y la desviación estándar

def main():
    # Leer los valores desde el usuario hasta que una línea en blanco es entrada.
    values = []
    s = input("Entra un valor (blanco para salir): ")
    while s != "":
        values.append(float(s))
        s = input("Entra un valor (blanco para salir): ")
    # Mostrar el resultado o un mensaje de error apropiado
    if len(values) < 2:
        print("No puedes entrar muchos valores.")
    else:
        stats = calculateStats(values)
        print("La media es", stats[0], "y la desviación estándar es", stats[1])

# Llamar a la función principal si este archivo no ha sido importado
if __name__ == "__main__":
    main()

##
# Lee una colección de palabras entradas por el usuario. Muestra cada palabra en el
# orden entrado por el usuario una vez en el mismo orden que las palabras fueron entradas

# Comenzar con una lista vacía
words = []
word = input("Entre una palabra (en blanco para salir): ")
while word != "":
    #Solamente adiciono la palabra en la lista si no está ya presente en esta
    if word not in words:
         words.append(word)
    #Leer la siguiente palabra
    word = input("Entre una palabra (en blanco para salir): ")

# Mostrar las palabras en el orden entrado por el usuario
print("Las palabras que entraste son: ")       
for word in words:
    print(word)



##
# Lee una colección de enteros entrados por el usuario. Muestra todos los negativos, 
# seguidos por todos los ceros, seguidos por todos los positivos.
#

# Comenzar con tres listas vacías
negatives = []  # Almacena los valores negativos
zeros = []      # Almacena los valores cero     
positives = []  # Almacena los valores positivos

# Leer los valores desde el usuario hasta que una línea en blanco es entrada
num = int(input("Entre un entero (en blanco para salir): "))
while num != 0:
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        positives.append(num)
    num = int(input("Entre un entero (en blanco para salir): "))

# Mostrar los valores en el orden requerido
for n in negatives:
    print(n)
for z in zeros:
    print(z)
for p in positives:
    print(p)
    

##
# Números perfectos: Un numero es perfecto si la suma de sus divisores propios es igual al número.
# Por ejemplo, 6 es perfecto porque 1+2+3 = 6. Este programa  muestra todos los números perfectos
# menores que un límite (LIMIT) dado.
# Define the properDivisors function directly in the script
def properDivisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Definir el límite
LIMIT = 10000

# @param n el número a verificar
# @return True si n es perfecto y False de lo contrario
def isPerfect(n):
    # Obtener una lista de los divisores propios de n
    divisors = properDivisors(n)
    # Calcular la suma de los divisores propios
    sum_divisors = 0
    for d in divisors:
        sum_divisors += d
    # Retornar si n es perfecto o no
    if sum_divisors == n:
        return True
    else:
        return False
    
# Mostrar todos los números perfectos menores que LIMIT
def main():
    print("Los números perfectos entre 1 y ", LIMIT, "son:")
    for i in range(1, LIMIT):
        if isPerfect(i):
            print(" ", i)    
# Call the main function if this script is executed
if __name__ == "__main__":
    main()

##
# Números primos: Un número es primo si es divisible solamente por 1 y por sí mismo.
# Este programa muestra todos los números primos menores que un límite (LIMIT) dado.       
# Define the properDivisors function directly in the script
def properDivisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Definir el límite
LIMIT = 10000

# @param n el número a verificar
# @return True si n es primo y False de lo contrario
def isPrime(n):
    # Obtener una lista de los divisores propios de n
    divisors = properDivisors(n)
    # Retornar si n es primo o no
    if len(divisors) == 1:
        return True
    else:
        return False
    
# Mostrar todos
# los números primos menores que LIMIT
def main():
    print("Los números primos entre 1 y ", LIMIT, "son:")
    for i in range(1, LIMIT):
        if isPrime(i):
            print(" ", i)
# Call the main function if this script is executed
if __name__ == "__main__":
    main()

##
# Formateando una lista
# Mostrar una lista de items donde estos estén separados por commas y la 
# palabra "and" antes de los dos últimos items.

# 
# @param items la lista de items a mostrar
# @return una cadena que contiene los items formateados 
#
def formatList(items):
    # Manejar el caso especial de una lista vacía
    if len(items) == 0:
        return "<empty>"
    # Manejar el caso especial de una lista con un solo item 
    if len(items) == 1:
        return items[0]
    # Construir la cadena de items excepto los dos últimos
    result = ""
    for i in range(0, len(items) - 2):
       result = result + str(items[i]) + ", "
    # Agregar el penúltimo item y el último item al resultado, separado por "and"
    result = result + str(items[-2]) + " and " + str(items[-1])
    # Retornar el resultado 
    return result

##
# Mostrar una lista de items formateados entrada por el usuario
#
def main():
    # Leer los items desde el usuario hasta que una línea en blanco es entrada
    items = []
    s = input("Entre un item (en blanco para salir): ")
    while s != "":
        items.append(s)
        s = input("Entre un item (en blanco para salir): ")
    # Mostrar los items formateados
    print("Los items son: ", formatList(items))

# Llamar a la función principal si este archivo no ha sido importado
if __name__ == "__main__":
    main()