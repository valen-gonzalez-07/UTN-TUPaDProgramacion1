# EJERCICIO 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea
# ------- RESPUESTA: 
# for i in range(101):
#     print(f"{i} ")


# EJERCICIO 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 
# ------- RESPUESTA: 
# numero = int(input("Ingresá un número entero: "))
# numero_str = str(abs(numero))
# print(f'La cantidad de dígitos del número es: {len(numero_str)}')


# EJERCICIO 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
# ------- RESPUESTA: 
# suma = 0
# num_1 = int(input("Ingresá el número A: "))
# num_2 = int(input("Ingresá el número B: "))
# if num_1 < num_2: 
#     for i in range(num_1+1, num_2): 
#         suma += i
# elif num_1 > num_2:
#     for i in range(num_2+1, num_1): 
#         suma += i
# else: 
#     suma = 0
# print(f'La suma de los números entre A y B es: {suma}')


# EJERCICIO 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 
# ------- RESPUESTA: 
# corte = 0
# suma = 0
# numero = int(input("Ingresá un número entero (0 para cortar): "))
# while numero != corte:
#     suma += numero
#     numero = int(input("Ingresá otro número entero (0 para cortar): "))
# print(f'La suma de los números es: {suma}')


# EJERCICIO 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
# ------- RESPUESTA: 
# import random 
# numero_aleatorio = random.randint(0, 9)
# numero_usuario = int(input("Ingresá un número entre 0 y 9: "))
# cont = 1
# while numero_usuario != numero_aleatorio: 
#     numero_usuario = int(input("No es :(. Intentá con otro: "))
#     cont += 1
# print(f"Adivinaste! El número era {numero_aleatorio}. Necesitaste {cont} intentos.")


# EJERCICIO 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 
# ------- RESPUESTA: 
# for i in range(101, -1, -1):
#     if i % 2 == 0:
#         print(f'{i} ', end="")


# EJERCICIO 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario. 
# ------- RESPUESTA: 
# num_1 = 0
# num_2 = int(input("Ingresá un número entero positivo: "))
# suma = 0
# while num_2 < 0: 
#     num_2 = int(input("Ingresá un número entero positivo: "))
# for i in range(num_2+1):
#     suma += i
# print(f'La suma de los números entre 0 y {num_2} es: {suma}')


# EJERCICIO 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# ------- RESPUESTA: 
# cantidad_permitida = 100 
# pares = 0 
# impares = 0 
# positivos = 0 
# negativos = 0 

# for i in range(cantidad_permitida):
#     numero = int(input("Ingresá un número entero: ")) 
#     if numero % 2 == 0: 
#         pares += 1
#     else: 
#         impares += 1
#     if numero == 0:
#         pass 
#     elif numero > 0: 
#         positivos += 1 
#     else: 
#         negativos += 1
# print(f'La cantidad de números pares es de: {pares}')
# print(f'La cantidad de números impares es de: {impares}')
# print(f'La cantidad de números positivos es de: {positivos}')
# print(f'La cantidad de números negativos es de: {negativos}') 


# EJERCICIO 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
# ------- RESPUESTA: 
# from statistics import mean 
# numeros_totales = []
# cantidad_permitida = 100 
# for i in range (cantidad_permitida): 
#     numero = int(input("Ingresá un número entero: ")) 
#     numeros_totales.append(numero)
# print(f'La media es: {mean(numeros_totales)}')


# EJERCICIO 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
# numero = input("Ingresá un número: ")
# numero_invertido = numero[::-1]  
# print(f"El número invertido es: {numero_invertido}")