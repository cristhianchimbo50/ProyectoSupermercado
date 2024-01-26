# Inicio de Sesión
print("Bienvenido Usuario")

# inicializar de productos y cantidades
Producto1, cantidadArroz = "Arroz", 0
# Producto1 = "Arroz"
# cantidadArroz = 0
Producto2, cantidadCola = "Cola", 0
Producto3, cantidadHelado = "Helado", 0
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

        if intentos == 3 :
            print("Ha superado el maximo de intentos.\n")
            raise SystemExit


while True:
    print("\n\n----- Menú de Inventario -----")
    print("1. Agregar Producto")
    print("2. Actualizar Existencias")
    print("3. Eliminar Producto")
    print("4. Mostrar Inventario")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("Agregar Producto...\n")
        nombre_producto = input("Ingrese el nombre del nuevo producto: ")
        existencias = int(input("Ingrese las existencias iniciales: "))

        #existencias es la cantidad que existe de X producto
        if nombre_producto == "Arroz":
            cantidadArroz = cantidadArroz + existencias
        elif nombre_producto == "Cola":
            cantidadArroz = cantidadArroz + existencias
        elif nombre_producto == "Helado":
            cantidadHelado = cantidadHelado + existencias
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
        print(Producto1 + ": " + str(cantidadArroz) + " unidades")
        print(Producto2 + ": " + str(cantidadCola) + " unidades")
        print(Producto3 + ": " + str(cantidadHelado) + " unidades")


    elif opcion == '5':
        print("Cerrando el Sistema")
        raise SystemExit

    else:
        print("Opción invalida, intentar nuevamente.")
