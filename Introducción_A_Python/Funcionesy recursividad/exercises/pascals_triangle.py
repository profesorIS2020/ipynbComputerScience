"""
https://es.wikipedia.org/wiki/Tri%C3%A1ngulo_de_Pascal
"""
"""
En Python, la expresión result[-1] se utiliza para acceder al último elemento de una lista llamada result.

En Python, los índices negativos se utilizan para acceder a los elementos de una lista empezando desde el final. Específicamente:

result[-1] accede al último elemento de la lista.
result[-2] accede al penúltimo elemento de la lista.
result[-3] accede al antepenúltimo elemento de la lista.
Y así sucesivamente.
Por ejemplo, si tienes una lista result definida de la siguiente manera:

python
Copiar código
result = [10, 20, 30, 40, 50]
Entonces:

result[0] sería 10 (el primer elemento).
result[1] sería 20 (el segundo elemento).
result[-1] sería 50 (el último elemento).
result[-2] sería 40 (el penúltimo elemento).
Esta característica es muy útil para acceder rápidamente a los elementos de una lista desde el final, sin tener que calcular manualmente la longitud de la lista.
"""
#La función len devuelve el número de valores de un elemento iterable enPython. 
def pascals_triangle(n):
    """ Recursive function to calculate Pascals Triangle """
    if n == 1:
        return [[1]] # Base case termination condition
    else:
        result = pascals_triangle(n-1) # Recursive call
        # Calculate current row using info from previous row
        current_row = [1]
        print('Este es el current_row ',current_row)
        previous_row = result[-1] # Take from end of result
        print('Este es el previus_row ', previous_row)
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
            print('Este es el current_row append ', previous_row)
        current_row += [1]
        print('Este es el current_row += ', current_row)
        result.append(current_row)
        print('result', result)
        return result


triangle = pascals_triangle(5)
for row in triangle:
    print(row)
