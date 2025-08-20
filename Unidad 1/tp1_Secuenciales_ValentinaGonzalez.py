# Práctico 1: Estructuras secuenciales 

# EJERCICIO 1: 
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
# ----------- RESPUESTA: 
# print("Hola Mundo!")

# EJERCICIO 2: 
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# ----------- RESPUESTA: 
# nombre = input("Ingresá tu nombre: ")
# saludo = f"Hola {nombre}!"
# print(saludo)

# EJERCICIO 3: 
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# ----------- RESPUESTA: 
# nombre = input("Ingresá tu nombre: ")
# apellido = input("Ingresá tu apellido: ")
# edad = input("Ingresá tu edad: ")
# residencia = input("Ingresá tu lugar de residencia: ")
# output = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
# print(output)

# EJERCICIO 4: 
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
# ----------- RESPUESTA: 
# radio = input("Ingresá el radio del círculo: ")
# radio = int(radio) 
# area = 3.1416 * radio * radio 
# perimetro = 2 * 3.1416 * radio 
# output = f"El área del círculo es {area} y el perimetro es {perimetro}"
# print(output)

# EJERCICIO 5: 
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
# ----------- RESPUESTA: 
# segundos = input("Ingresá una cantidad de segundos: ")
# horas = (float(segundos) / 60) / 60 
# output = f"{segundos} son {horas} horas"
# print(output)


# EJERCICIO 6: 
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 
# ----------- RESPUESTA: (uso el bucle for porque lo conozco de antes)
# numero = input("Ingresá un número: ")
# numero = int(numero)
# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

# EJERCICIO 7: 
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
# ----------- RESPUESTA: 
# numero1 = int(input("Ingresá un número entero distinto de 0: "))
# numero2 = int(input("Ingresá otro número entero distinto de 0: "))
# suma = numero1 + numero2
# division = numero1 / numero2
# multiplicacion = numero1 * numero2 
# resta = numero1 - numero2 
# print(f"Suma: {suma}")
# print(f"División: {division}")
# print(f"Multiplicación: {multiplicacion}")
# print(f"Resta: {resta}")

# EJERCICIO 8: 
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# ----------- RESPUESTA: 
# altura = float(input("Ingresá tu altura en metros: "))
# peso = float(input("Ingresá tu peso en kg: "))
# imc = peso / (altura ** 2)
# print(f"Tu IMC es de {imc}")

# EJERCICIO 9: 
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
# ----------- RESPUESTA: 
# temperatura = float(input("Ingresá una temperatura en grados Celsius: "))
# equivalente = (9 / 5) * temperatura + 32 
# print(f"El equivalente en grados Fahrenheit es {equivalente}")

# EJERCICIO 10: 
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
# ----------- RESPUESTA: 
# numero1 = float(input("Ingresá un número: "))
# numero2 = float(input("Ingresá otro número: "))
# numero3 = float(input("Ingresá otro número: ")) 
# promedio = (numero1 + numero2 + numero3) / 3
# print(f"El promedio es de: {promedio}")