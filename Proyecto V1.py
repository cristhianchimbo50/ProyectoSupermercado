# Inicio de Sesión
print("Bienvenido Usuario")

intentos = 0

while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == '1' and contrasena == '1':
        print("Inicio de sesión exitoso.\n")
        break
    else:
        print("\n\nNombre de usuario o contraseña incorrectos, intentar nuevamente.")

        intentos = intentos + 1

        if intentos == 3:
            print("Ha superado el máximo de intentos.\n")
            raise SystemExit

# Inventario
inventario = {}

while True:
    print("\n----- Menú de Inventario -----")
    print("1. Agregar Producto")
    print("2. Actualizar Stock")
    print("3. Eliminar Producto")
    print("4. Mostrar Inventario")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre_producto = input("Ingrese el nombre del nuevo producto: ")
        stock = int(input("Ingrese el Stock inicial: "))
        inventario[nombre_producto] = stock
        print("Producto agregado con éxito.")

    elif opcion == '2':
        nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
        if nombre_producto in inventario:
            stock = int(input("Ingrese las nuevas existencias: "))
            inventario[nombre_producto] = stock
            print("Stock actualizado con éxito.")
        else:
            print("Producto no encontrado en el inventario.")

    elif opcion == '3':
        nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
        if nombre_producto in inventario:
            del inventario[nombre_producto]
            print("Producto eliminado con éxito.")
        else:
            print("Producto no encontrado en el inventario.")

    elif opcion == '4':
        print("\nInventario:")
        for producto, stock in inventario.items():
            print(f"{producto}: {stock} unidades")

    elif opcion == '5':
        print("Cerrando el Sistema")
        raise SystemExit

    else:
        print("Opción inválida, intentar nuevamente.")
