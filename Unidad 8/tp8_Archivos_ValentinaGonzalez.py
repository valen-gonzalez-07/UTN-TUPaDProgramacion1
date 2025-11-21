# ACTIVIDAD 1: Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

productos = [
    "Lapicera,500,75\n",
    "Lapiz,300,100\n",
    "Cuadernillo,5500,40\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)



# ACTIVIDAD 2: Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el 
# siguiente formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

print("\n====================")
print("Actividad 2: ")

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = float(partes[1])
        cantidad = int(partes[2])
        print(f"Producto: {nombre.capitalize()} | Precio: ${precio} | Cantidad: {cantidad}")


# ACTIVIDAD 3: Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("\n====================")
print("Actividad 3: ")

nombre_nuevo_producto = ''

while True:
    nombre_nuevo_producto = input("Ingresá un nuevo producto: ").strip()
    if(nombre_nuevo_producto == ''):
        break
    precio = float(input("Ingresá el precio del producto: "))
    cantidad = int(input("Ingresá la cantidad: "))
    nuevo_producto = f"{nombre_nuevo_producto},{precio},{cantidad}\n"
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nuevo_producto}\n")


# ACTIVIDAD 4: Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad

print("\n====================")
print("Actividad 4: ")

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    productos = []
    for linea in lineas:
        if linea.strip() == "": 
            continue
        partes = linea.strip().split(",")
        dic = {
            "nombre": partes[0].capitalize(),
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        productos.append(dic)

for producto in productos: 
    print(producto)


# ACTIVIDAD 5: Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

print("\n====================")
print("Actividad 5: ")

producto_a_consultar = input("Ingresá un producto a consultar: ").lower()
encontrado = False

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        if linea.strip() == "":
            continue
        partes = linea.strip().split(",")
        nombre, precio, cantidad = partes
        if nombre.lower() == producto_a_consultar:
            print(f"Producto: {nombre.capitalize()} | Precio: ${precio} | Cantidad: {cantidad}")
            encontrado = True
            break

if not encontrado:
    print("El producto que ingresaste no existe.")



# EJERCICIO 6: Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

print("\n====================")
print("Actividad 6: ")

with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f'{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n'
        archivo.write(linea)

with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)