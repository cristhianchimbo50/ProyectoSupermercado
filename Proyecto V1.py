# Inicio de Sesión
print("Bienvenido Usuario")

# Inicialización de productos y existencias
producto1, existencia1 = "Producto1", 0
producto2, existencia2 = "Producto2", 0
producto3, existencia3 = "Producto3", 0

while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == 'usuario1' and contrasena == 'contrasena1':
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Nombre de usuario o contraseña incorrectos. Inténtelo nuevamente.")

while True:
    print("\n----- Menú de Inventario -----")
    print("1. Agregar Producto")
    print("2. Actualizar Existencias")
    print("3. Eliminar Producto")
    print("4. Mostrar Inventario")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        nombre_producto = input("Ingrese el nombre del nuevo producto: ")
        existencias = int(input("Ingrese las existencias iniciales: "))
        if nombre_producto == "Producto1":
            existencia1 += existencias
        elif nombre_producto == "Producto2":
            existencia2 += existencias
        elif nombre_producto == "Producto3":
            existencia3 += existencias
        else:
            print("Producto no válido. Inténtelo nuevamente.")

        print("Producto agregado con éxito.")

    elif opcion == '2':
        nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
        existencias = int(input("Ingrese las nuevas existencias: "))
        if nombre_producto == "Producto1":
            existencia1 = existencias
        elif nombre_producto == "Producto2":
            existencia2 = existencias
        elif nombre_producto == "Producto3":
            existencia3 = existencias
        else:
            print("Producto no encontrado. Inténtelo nuevamente.")

        print("Existencias actualizadas con éxito.")

    elif opcion == '3':
        nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
        if nombre_producto == "Producto1":
            existencia1 = 0
        elif nombre_producto == "Producto2":
            existencia2 = 0
        elif nombre_producto == "Producto3":
            existencia3 = 0
        else:
            print("Producto no encontrado. Inténtelo nuevamente.")

        print("Producto eliminado con éxito.")

    elif opcion == '4':
        print("\nInventario:")
        print(f"{producto1}: {existencia1} unidades")
        print(f"{producto2}: {existencia2} unidades")
        print(f"{producto3}: {existencia3} unidades")

    elif opcion == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Inténtelo nuevamente.")
