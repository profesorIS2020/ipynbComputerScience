"""En matemáticas, un número primo es un número natural mayor que 1 que tiene únicamente dos divisores positivos distintos: él mismo y el 1.Por el contrario, los números compuestos son los números naturales que tienen algún divisor natural aparte de sí mismos y del 1, y, por lo tanto, pueden factorizarse. El número 1, por convenio, no se considera ni primo ni compuesto.
"""

def is_prime(n, i=2):
    # Base cases
    if n <= 2:
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return True

    # Check for next divisor
    return is_prime(n, i + 1)


print('is_prime(3):', is_prime(3))
print('is_prime(7):', is_prime(7))
print('is_prime(9):', is_prime(9))
print('is_prime(31):', is_prime(31))
