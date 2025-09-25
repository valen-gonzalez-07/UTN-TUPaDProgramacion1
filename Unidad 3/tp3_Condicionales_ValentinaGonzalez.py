# Práctico 3: Estructuras Condicionales

# EJERCICIO 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 
# ----------- RESPUESTA: 
# edad = int(input("Ingresá tu edad: "))
# if edad >= 18: 
#     print("Es mayor de edad.")
# else: 
#     print("Es menor de edad.")


# EJERCICIO 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 
# ----------- RESPUESTA: 
# nota = int(input("Ingresá tu nota: "))
# if nota >= 6:
#     print("Aprobado!")
# else: 
#     print("Desaprobado.")


# EJERCICIO 3:  Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# ----------- RESPUESTA: 
# num = int(input("Ingresá un número: "))
# if num % 2 == 0: 
#     print("Ha ingresado un número par.")
# else: 
#     print("Por favor, ingrese un número par.")


# EJERCICIO 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece. 
# ----------- RESPUESTA: 
# edad = int(input("Ingresá tu edad: "))
# if edad < 12: 
#     print("Categoría: Niño/a.")
# elif edad >= 12 and edad < 18:
#     print("Categoría: Adolescente.")
# elif edad >= 18 and edad < 30:
#     print("Categoría: Adulto/a joven.")
# else: 
#     print("Categoría: Adulto/a.")


# EJERCICIO 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# ----------- RESPUESTA: 
# password = input("Ingresá una contraseña: ")
# if len(password) >= 8 and len(password) <= 14:
#     print("Ingresaste una contraseña correcta.")
# else:
#     print("Por favor, ingresá una contraseña de entre 8 y 14 caracteres.")


# EJERCICIO 6: Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# ----------- RESPUESTA: 
# from  statistics import mode, median, mean
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# param_media = mean(numeros_aleatorios)
# param_mediana = median(numeros_aleatorios) 
# param_moda = mode(numeros_aleatorios)
# print("Números:", numeros_aleatorios)
# if param_media > param_mediana > param_moda:
#     print("Hay sesgo positivo.")
# elif param_media < param_mediana < param_moda:
#     print("Hay sesgo negativo.")
# elif param_media == param_mediana == param_moda: 
#     print("No hay sesgo.")
# else: 
#     print("No se cumple ninguna condición exacta para clasificar.")


# EJERCICIO 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
# ----------- RESPUESTA: 
# palabra = input("Ingresá una frase o palabra: ")
# ultimo_caracter = palabra[-1]
# vocales = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
# if ultimo_caracter in vocales:
#     print(palabra, '!')
# else:
#     print(palabra)


# EJERCICIO 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee. 
# ----------- RESPUESTA: 
# nombre = input("Ingresá tu nombre: ")
# print("Ingresá la opción que deseas para transformarlo, siendo: ")
# print("1: Si lo querés en mayúsculas.")
# print("2: Si lo querés en minúsculas.")
# print("3: Si lo querés con la primera letra mayúscula.")
# opt = int(input("Seleccioná la opción deseada: "))
# if opt == 1: 
#     print(nombre.upper())
# elif opt == 2: 
#     print(nombre.lower())
# elif opt == 3:
#     print(nombre.title())
# else:
#     print("La opción seleccionada no corresponde.")


# EJERCICIO 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ----------- RESPUESTA: 
# magnitud = float(input("Ingresá la magnitud del terremoto: "))
# if magnitud >= 7:
#     print("Extremo (puede causar graves daños a gran escala).")
# elif magnitud >= 6 and magnitud < 7: 
#     print("Muy Fuerte (puede causar daños significativos).")
# elif magnitud >= 5 and magnitud < 6: 
#     print("Fuerte (puede causar daños en estructuras débiles).")
# elif magnitud >= 4 and magnitud < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños).")
# elif magnitud >= 3 and magnitud < 4:
#     print("Leve (ligeramente perceptible).")
# else: 
#     print("Muy leve (imperceptible).")


# EJERCICIO 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
# ----------- RESPUESTA: 
# hemisferio = input("Ingresá en qué hemisferio te encontrás (N/S): ").upper()
# mes = int(input("Ingresá el mes del año (1 al 12): "))
# dia = int(input("Ingresá el día (1 al 31): "))
# if hemisferio == "N": 
#     if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#         estacion = "Invierno"
#     elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#         estacion = "Primavera"
#     elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#         estacion = "Verano"
#     else:
#         estacion = "Otoño"
# elif hemisferio == "S": 
#     if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#         estacion = "Verano"
#     elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#         estacion = "Otoño"
#     elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#         estacion = "Invierno"
#     else:
#         estacion = "Primavera"
# else:
#     estacion = "El hemisferio es inválido"
# print(estacion)