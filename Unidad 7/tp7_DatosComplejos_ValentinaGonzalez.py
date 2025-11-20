# EJERCICIO 1: Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios: Naranja = 1200, Manzana = 1500, Pera = 2300

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# print(f"Ejercicio 1: {precios_frutas}")

# EJERCICIO 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en 
# el punto anterior, actualizar los precios de las siguientes frutas: Banana = 1330, Manzana = 1700, Melón = 2800 

# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# print(f"Ejercicio 2: {precios_frutas}")

# EJERCICIO 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 

# lista_frutas = list(precios_frutas.keys())
# print(f"Ejercicio 3: {lista_frutas}")


# ---------------------------------------- 
# EJERCICIO 4: Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe 
# ---------------- RESPUESTA: 

# contactos = {}

# for i in range(5): 
#     nombre = input("Ingresá el nombre del contacto: ").lower()
#     numero = int(input("Ingresá el número telefónico: "))
#     contactos[nombre] = numero

# print("=========================================")
# nombre_a_consultar = input("Ingresá el nombre del contacto a consultar: ").lower()
# if nombre_a_consultar in contactos:
#     print(f"El número de {nombre_a_consultar.capitalize()} es: {contactos[nombre_a_consultar]}")
# else:
#     print("El contacto no existe.")


# ---------------------------------------- 
# EJERCICIO 5: Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. 
# ---------------- RESPUESTA: 

# frase = input("Escribí una frase: ")
# lista_palabras = frase.split(' ')

# palabras_unicas = set(frase.split(' '))
# print(f"Palabras únicas: {palabras_unicas}")

# cantidad = {}

# for palabra in lista_palabras: 
#     if palabra in cantidad:
#         cantidad[palabra] += 1
#     else:
#         cantidad[palabra] = 1

# print(f"Cantidad de veces por palabra: {cantidad}")


# ---------------------------------------- 
# EJERCICIO 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno. 
# ---------------- RESPUESTA: 

# alumnos = {}

# for i in range(3): 
#     nombre = input("Ingresá el nombre del alumno: ").lower()
#     notas = ()
#     for j in range(1,4): 
#         nota = int(input(f"Ingresá la nota {i}: "))
#         notas = notas + (nota,)
#     alumnos[nombre] = notas

# for alumno in alumnos: 
#     notas = alumnos[alumno]
#     a, b, c = notas
#     promedio = (a + b + c) / 3
#     print(f"El promedio de {alumno} es {promedio}")


# ---------------------------------------- 
# EJERCICIO 7: Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
# ---------------- RESPUESTA: 

# aprobaron_parcial1 = {7, 8, 9, 9, 10, 7}
# aprobaron_parcial2 = {9, 7, 8, 7, 7, 7}

# aprobaron_ambos = aprobaron_parcial1 & aprobaron_parcial2 
# aprobaron_solo_uno = aprobaron_parcial1 ^ aprobaron_parcial2
# aprobaron_al_menos_uno = aprobaron_parcial1 | aprobaron_parcial2

# print(f"Aprobaron ambos parciales {aprobaron_ambos} estudiantes.")
# print(f"Aprobaron solo un parcial {aprobaron_solo_uno} estudiantes.")
# print(f"Aprobaron al menos un parcial {aprobaron_al_menos_uno} estudiantes.")


# ---------------------------------------- 
# EJERCICIO 8: Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
# ---------------- RESPUESTA: 

# productos = {}

# def imprimirListadoProductos(): 
#     print("\nListado actual de productos:")
#     for producto in productos: 
#         print(f"• {producto.capitalize()}")

# def consultarStock():
#     producto = input("\nIngresá el producto: ").lower()
#     if producto in productos:
#         print(f"\nEl stock de {producto.upper()} es de {productos[producto]} unidades.")
#     else: 
#         print("El producto no está en el listado.")

# def agregarUnidades():
#     producto = input("\nIngresá el producto: ").lower()
#     if producto in productos: 
#         cantidad_a_agregar = int(input("Cantidad de unidades a agregar: "))
#         productos[producto] += cantidad_a_agregar
#         print(f"\nEl stock de {producto.upper()} ahora es de {productos[producto]} unidades.")
#     else: 
#         print("El producto no está en el listado.")

# def agregarProducto():
#     producto = input("\nIngresá el producto: ").lower()
#     if producto in productos: 
#         print("El producto ya está agregado.")
#     else:
#         stock = int(input("Ingresá el stock: "))
#         productos[producto] = stock
#         imprimirListadoProductos()

# option = ""

# while option != "fin": 
#     producto = input("Ingresá el nombre del producto o 'FIN' para finalizar: ").lower()
#     option = producto
#     if(option == "fin"): 
#         break
#     stock = int(input("Ingresá el stock: "))
#     productos[producto] = stock

# print("\n==================")
# print("Los productos fueron agregados correctamente.")
# print("==================") 

# option_menu = ""

# while option_menu != "fin": 
#     print("\nMENÚ:")
#     print("1: Consultar stock")
#     print("2: Agregar unidades al stock")
#     print("3: Agregar nuevo producto")

#     option_menu_str = input("\nIngresá la opción que deseás o 'FIN' para finalizar: ").strip()
#     if option_menu_str.isdigit():
#         option_menu = int(option_menu_str)
#     else:
#         option_menu = 0 

#     if(option_menu_str.lower() == "fin"):
#         break

#     if option_menu <= 0 or option_menu > 3:
#         print("==================") 
#         print("La opción elegida no está entre las permitidas. Intentá nuevamente.")
#         print("==================") 
#         continue 
#     else: 
#         match option_menu:
#             case 1: 
#                 imprimirListadoProductos()  
#                 consultarStock()
#             case 2: 
#                 imprimirListadoProductos()
#                 agregarUnidades()
#             case 3:
#                 agregarProducto()


# ---------------------------------------- 
# EJERCICIO 9: Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora.
# ---------------- RESPUESTA: 

# agenda = {
#     ("lunes", "10:00"): "Daily",
#     ("lunes", "13:00"): "Hand off",
#     ("lunes", "15:00"): "Call para definición de sprint 1",
#     ("martes", "10:00"): "Daily",
#     ("martes", "15:00"): "Call de seguimiento sprint 1",
#     ("miercoles", "10:00"): "Daily",
#     ("miercoles", "17:30"): "Hand off",
#     ("jueves", "10:00"): "Daily",
#     ("viernes", "10:00"): "Daily",
#     ("viernes", "15:00"): "Call de seguimiento sprint 1",
# }

# dia = input("Ingresá el día: ").lower()
# hora = input("Ingresá la hora (ej: 10:00): ")

# key = (dia, hora)

# if key in agenda: 
#     print(f"Evento: {agenda[key]}")
# else: 
#     print("No hay eventos agendados para ese día y hora.")


# ---------------------------------------- 
# EJERCICIO 9: Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. 

paises_y_capitales = {
    "Argentina" : "Ciudad Autónoma de Buenos Aires",
    "Bolivia" : "Sucre",
    "Perú" : "Lima",
    "Brasil" : "Brasilia",
    "Chile" : "Santiago de Chile",
    "Venezuela" : "Caracas",
}

capitales_y_paises = {}

for pais, capital in paises_y_capitales.items(): 
    capitales_y_paises[capital] = pais

print(f"Países con sus capitales: {paises_y_capitales}")
print(f"Capitales con sus países: {capitales_y_paises}")

