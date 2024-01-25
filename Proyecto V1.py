# Inicio de Sesión
print("Bienvenido Usuario")

# Inicialización de productos y cantidades
Arroz, cantidadArroz = "Arroz", 0
Cola, cantidadCola = "Cola", 0
Helado, cantidadHelado = "Helado", 0

while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == 'sebas' and contrasena == '12345':
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
        print("Agregar Producto...\n")
        nombre_producto = input("Ingrese el nombre del nuevo producto: ")
        existencias = int(input("Ingrese las existencias iniciales: "))
        if nombre_producto == "Arroz":
            cantidadArroz += existencias
        elif nombre_producto == "Cola":
            cantidadCola += existencias
        elif nombre_producto == "Helado":
            cantidadHelado += existencias
        else:
            print("Producto no válido. Inténtelo nuevamente.")

        print("Producto agregado con éxito.")

    elif opcion == '2':
        print("Actualizar Existencia...\n")
        nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
        existencias = int(input("Ingrese las nuevas existencias: "))
        if nombre_producto == "Arroz":
            cantidadArroz = existencias
        elif nombre_producto == "Cola":
            cantidadCola = existencias
        elif nombre_producto == "Helado":
            cantidadHelado = existencias
        else:
            print("Producto no encontrado. Inténtelo nuevamente.")

        print("Existencias actualizadas con éxito.")

    elif opcion == '3':
        print("Eliminar Producto...\n")
        nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
        if nombre_producto == "Arroz":
            cantidadArroz = 0
        elif nombre_producto == "Cola":
            cantidadCola = 0
        elif nombre_producto == "Helado":
            cantidadHelado = 0
        else:
            print("Producto no encontrado. Inténtelo nuevamente.")

        print("Producto eliminado con éxito.")

    elif opcion == '4':
        print("\nInventario:")
        print(f"{Arroz}: {cantidadArroz} unidades")
        print(f"{Cola}: {cantidadCola} unidades")
        print(f"{Helado}: {cantidadHelado} unidades")

    elif opcion == '5':
        print("chao")
        break

    else:
        print("Opción no válida. Inténtelo nuevamente.")
