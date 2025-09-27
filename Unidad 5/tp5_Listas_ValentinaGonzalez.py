# EJERCICIO 1: Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja 
# ---------------- RESPUESTA: 
# notas = [6, 7, 4, 2, 10, 9, 9, 8, 7, 4]
# promedio = sum(notas) / 10
# nota_mas_alta = 0
# nota_mas_baja = float('inf')
# for i in range(len(notas)): 
#     if notas[i] > nota_mas_alta:
#         nota_mas_alta = notas[i]
#     if notas[i] < nota_mas_baja:
#         nota_mas_baja = notas[i]
# print(f'El listado de notas es: {notas}')
# print(f'El promedio entre las notas es: {promedio}')
# print(f'La nota más alta es: {nota_mas_alta}')
# print(f'La nota más baja es: {nota_mas_baja}')


# EJERCICIO 2: Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista
# ---------------- RESPUESTA:
# productos = []
# for i in range(5): 
#     producto = input("Ingresá un producto: ")
#     productos.append(producto)
# productos_ordenados = sorted(productos)
# print(f'Los productos son: {productos_ordenados}')
# producto_a_eliminar = input(f'¿Qué producto deseás eliminar?: ')
# if producto_a_eliminar in productos_ordenados:
#     productos_ordenados.remove(producto_a_eliminar)
#     print(f'La lista actualizada es: {productos_ordenados}')
# else:
#     print('Ese producto no está en la lista.')


# EJERCICIO 3: Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista. 
# ---------------- RESPUESTA: 
# import random 
# numeros_aleatorios =  random.sample(range(1, 101), 15) 
# numeros_pares = []
# numeros_impares = []
# for i in range(len(numeros_aleatorios)): 
#     if numeros_aleatorios[i] % 2 == 0:
#         numeros_pares.append(numeros_aleatorios[i])
#     else: 
#         numeros_impares.append(numeros_aleatorios[i])
# print(f'Números pares: {numeros_pares}. La lista tiene una cantidad de {len(numeros_pares)} números.')
# print(f'Números impares: {numeros_impares}. La lista tiene una cantidad de {len(numeros_impares)} números.')


# EJERCICIO 4: Dada una lista con valores repetidos: 
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado. 
# ---------------- RESPUESTA: 
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# datos_sin_repetir = set(datos)
# print(f'La lista original es: {datos}')
# print(f'La lista sin elementos repetidos es: {list(datos_sin_repetir)}')


# EJERCICIO 5: Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada. 
# ---------------- RESPUESTA: 
# nombres = ["Valentina", "Gina", "Lucia", "Lucas", "Franco", "Facundo", "Francisco", "Micaela"]
# print(f'Los nombres existentes son: {nombres}')
# agregar_o_eliminar = input("¿Desás agregar o eliminar un nuevo estudiante? (A para agregar - E para eliminar)")
# if agregar_o_eliminar == 'A' or agregar_o_eliminar == 'a':
#     nuevo_nombre = input("Ingresá un nuevo estudiante: ")
#     nombres.append(nuevo_nombre)
# elif agregar_o_eliminar == 'E' or agregar_o_eliminar == 'e': 
#     nombre_a_eliminar = input("Eliminá un estudiante existente: ")
#     nombre_a_eliminar = nombre_a_eliminar.title()
#     if(nombre_a_eliminar in nombres):
#         nombres.remove(nombre_a_eliminar)
# else:
#     print('La opción no es válida.')
# print(f'La nueva lista es: {nombres}')


# EJERCICIO 6: Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
# ---------------- RESPUESTA: 
# numeros = [1, 2, 3, 4, 5, 6, 7]
# numeros_rotados = [numeros[-1]] + numeros[:-1]
# print(f'La lista original es: {numeros}')
# print(f'La lista rotada es: {numeros_rotados}')


# EJERCICIO 7: Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica 
# ---------------- RESPUESTA: 
# matriz = [
#     [7, 14],
#     [12, 20],
#     [8, 16],
#     [14, 22],
#     [12, 20],
#     [9, 18],
#     [10, 20]
# ]
# minimas = []
# maximas = []
# for i in range(7): 
#     minimas.append(matriz[i][0])
#     maximas.append(matriz[i][1])   
# promedio_minimas = sum(minimas) / 7
# promedio_maximas = sum(maximas) / 7
# print(f'El promedio de las mínimas es de: {promedio_minimas}')
# print(f'El promedio de las máximas es de: {promedio_maximas}')
# amplitud_termica = 0
# dia_amplitud_termica = 0
# for i in range(7):
#     amplitud_dia = matriz[i][1] - matriz[i][0]
#     if amplitud_dia > amplitud_termica:
#         amplitud_termica = amplitud_dia 
#         dia_amplitud_termica = i + 1
# print(f'El día de mayor amplitud térmica fue el {dia_amplitud_termica} y la amplitud fue de {amplitud_termica}.')


# EJERCICIO 8: Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.
# ---------------- RESPUESTA: 
# notas = [
#     [6, 8, 7],
#     [5, 6, 7],
#     [5, 7, 6],
#     [8, 9, 7],
#     [4, 5, 6] 
# ]
# nombres = ["Lucía", "Gina", "Lucas", "Franco", "Valentina"]
# materias = ["Matemática", "Física", "Química"]
# for i in range(5):
#     promedio_alumno = sum(notas[i]) / len(notas[i])
#     print(f'Promedio de {nombres[i]}: {promedio_alumno}')
# print('===========')
# for j in range(3):
#     promedio_materia = sum(notas[i][j] for i in range(5)) / 5
#     print(f'Promedio de {materias[j]}: {promedio_materia}')


# EJERCICIO 9: Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
# ---------------- RESPUESTA: 
# matriz = [
#     [' - ', ' - ', ' - '],
#     [' - ', ' - ', ' - '],
#     [' - ', ' - ', ' - ']
# ]
# pos_X_a = int(input("Jugador 1, ingresá una posición de fila (0 a 2): "))
# pos_Y_a = int(input("Jugador 1, ingresá una posición de columna (0 a 2): "))
# pos_X_b = int(input("Jugador 2, ingresá una posición de fila (0 a 2): "))
# pos_Y_b = int(input("Jugador 2, ingresá una posición de columna (0 a 2): "))
# matriz[pos_X_a][pos_Y_a] = ' X '
# matriz[pos_X_b][pos_Y_b] = ' O '
# for fila in matriz:
#     print(fila)