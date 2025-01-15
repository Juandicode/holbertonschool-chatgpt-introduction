#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrementar n en cada iteración
    return result

# Asegurarse de que se pase un argumento y manejar posibles errores
if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: El factorial no está definido para números negativos.")
        else:
            f = factorial(num)
            print(f"Factorial de {num}: {f}")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
else:
    print("Uso: ./script.py <número>")
