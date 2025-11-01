# EJERCICIO 1: Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
# ---------------- RESPUESTA: 

# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# imprimir_hola_mundo() 


# ----------------------------------------
# EJERCICIO 2: Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario. 
# ---------------- RESPUESTA: 

# def saludar_usuario(nombre): 
#     print(f"Hola {nombre}!")

# nombreUsuario = input("Ingresá tu nombre: ")
# saludar_usuario(nombreUsuario)


# ---------------------------------------- 
# EJERCICIO 3: Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.
# ---------------- RESPUESTA: 

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# nombre = input("Ingresá tu nombre: ")
# apellido = input("Ingresá tu apellido: ")
# edad = input("Ingresá tu edad: ")
# residencia = input("Ingresá tu residencia: ")
# informacion_personal(nombre, apellido, edad, residencia)


# ---------------------------------------- 
# EJERCICIO 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
# ---------------- RESPUESTA:

# import math 

# def calcular_area_circulo(radio):
#     area = math.pi * (radio**2)
#     return print(f"El área del círculo es: {area}")

# def calcular_perimetro_circulo(radio):
#     perimetro = 2 * math.pi * radio 
#     return print(f"El perímetro del círculo es: {perimetro}")

# radio = int(input("Ingresá el radio del círculo: "))
# calcular_area_circulo(radio)
# calcular_perimetro_circulo(radio)


# ---------------------------------------- 
# EJERCICIO 5: Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
# ---------------- RESPUESTA: 

# def segundos_a_horas(segundos):
#     horas = (segundos / 60) / 60
#     return print(f"La cantidad de horas correspondientes a tus segundos es de: {horas}")

# segundos = int(input("Ingresá la cantidad de segundos: "))
# segundos_a_horas(segundos)


# ---------------------------------------- 
# EJERCICIO 6: Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
# ---------------- RESPUESTA: 

# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")

# numero = int(input("Ingresá un número: "))
# tabla_multiplicar(numero)


# ---------------------------------------- 
# EJERCICIO 7: . Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara 
# ---------------- RESPUESTA: 

# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b 
#     multiplicacion = a * b 
#     division = a / b 
#     print("Los resultados obtenidos son: ")
#     print(f"{a} + {b} = {suma}")
#     print(f"{a} - {b} = {resta}")
#     print(f"{a} * {b} = {multiplicacion}")
#     print(f"{a} / {b} = {division}")

# a = int(input("Ingresá el primer número: "))
# b = int(input("Ingresá el segundo número: "))
# operaciones_basicas(a, b)


# ---------------------------------------- 
# EJERCICIO 8: Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
# ---------------- RESPUESTA: 

# def calcular_imc(peso, altura):
#     imc = peso / (altura**2)
#     return print(f"Tu IMC es de: {imc}")

# peso = float(input("Ingresá tu peso (en kg): "))
# altura = float(input("Ingresá tu altura (en metros): "))
# calcular_imc(peso, altura)


# ---------------------------------------- 
# EJERCICIO 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
# ---------------- RESPUESTA: 

# def celsius_a_fahrenheit(celsius):
#     f = (celsius * 1.8) + 32
#     return print(f"{celsius} Celsius son equivalentes a {f} Fahrenheit.")

# celsius = float(input("Ingresá una temperatura en grados Celsius: "))
# celsius_a_fahrenheit(celsius)


# ---------------------------------------- 
# EJERCICIO 10: Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.
# ---------------- RESPUESTA: 

# def calcular_promedio(a, b, c): 
#     promedio = (a + b + c) / 3
#     return print(f"El promedio es: {promedio}")

# a = float(input("Ingresá el primer número: "))
# b = float(input("Ingresá el segundo número: "))
# c = float(input("Ingresá el tercer número: "))
# calcular_promedio(a, b, c)