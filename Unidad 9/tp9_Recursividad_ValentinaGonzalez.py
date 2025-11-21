# EJERCICIO 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# def factorial(x): 
#     return 1 if x == 0 else x * factorial(x - 1)

# num = int(input("Ingresá un número: "))

# for i in range(1, num + 1):
#     print(f"El factorial de {i} es {factorial(i)}")


# EJERCICIO 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# num = int(input("Ingresá una posición de Fibonacci: "))

# print("Serie completa:")
# for i in range(num + 1):
#     print(fibonacci(i), end=" ")


# EJERCICIO 3: Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     else:
#         return base * potencia(base, exponente - 1)

# base = float(input("Ingresá la base: "))
# exp = int(input("Ingresá el exponente: "))

# resultado = potencia(base, exp)
# print(f"{base} elevado a {exp} es {resultado}")


# EJERCICIO 4: Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto. 

# def decimal_a_binario(n):
#     if n < 2:  
#         return str(n)
#     else:
#         return decimal_a_binario(n // 2) + str(n % 2)

# num = int(input("Ingresá un número entero positivo: "))
# resultado = decimal_a_binario(num)
# print(f"El número {num} en binario es {resultado}")


# EJECICIO 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed()

# def es_palindromo(palabra):
#     if len(palabra) <= 1:
#         return True
#     if palabra[0] != palabra[-1]:
#         return False
#     return es_palindromo(palabra[1:-1])

# texto = input("Ingresá una palabra: ").lower()

# if es_palindromo(texto):
#     print(f"{texto} es un palíndromo")
# else:
#     print(f"{texto} NO es un palíndromo")


# EJERCICIO 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

# def suma_digitos(n):
#     if n < 10:
#         return n
#     return (n % 10) + suma_digitos(n // 10)

# num = int(input("Ingresá un número: "))
    
# print(suma_digitos(num))


# EJERCICIO 7: Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 

# def contar_bloques(n):
#     return 1 if n == 1 else n + contar_bloques(n - 1)

# num = int(input("Ingresá un número: "))
    
# print(contar_bloques(num))


# EJERCICIO 7: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

# def contar_digito(numero, digito):
#     if numero == 0:
#         return 0
    
#     ultimo = numero % 10
    
#     if ultimo == digito:
#         return 1 + contar_digito(numero // 10, digito)
#     else:
#         return contar_digito(numero // 10, digito)

# numero = int(input("Ingresá un número entero positivo: "))
# digito = int(input("Ingresá el dígito a buscar (0-9): "))

# if digito < 0 or digito > 9:
#     print("El dígito debe estar entre 0 y 9.")
# else:
#     resultado = contar_digito(numero, digito)
#     print(f"El dígito {digito} aparece {resultado} veces en {numero}.")