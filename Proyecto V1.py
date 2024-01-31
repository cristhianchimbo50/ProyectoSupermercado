# Inicialización de variables
i = 1
n = 10
intent = 0
ses = 0
opc = 0
vent = 0
suel_tot = 0
cant_pro = 0
exis_leche = 0
exis_atun = 0
exis_huevos = 0
exis_papel = 0
exis_alcohol = 0
exis_curitas = 0
exis_gasas = 0
exis_sal = 0
exis_cafe = 0
exis_arroz = 0
suma = 0
desc = 0
precio = 0
total_cancelar = 0
usu = ""
cont = ""
nom_prod = ""
resp = ""

        
while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == 'tienda' and contrasena == 'T2024':
        print("Inicio de sesión exitoso.\n")
        break
    else:
        print("\nEl usuario o contraseña es incorrecto\n")
        intent = intent + 1
        
        if intent == 3:
            print("\nUsuario bloqueado, utilizó 3 intentos\n")
            raise SystemExit

while True:
    print("**Bienvenidos al Sistema**")
    ses = 1
    print("\n**Bienvenidos al siguiente menú**\n")
    print("1. Visualizar el total a cancelar")
    print("2. Visualizar el bono de los empleados")
    print("\n**Inventario del Supermercado**\n")
    print("\nBienvenidos al siguiente menú\n")
    print("3. Agregar productos y muestra el inventario")
    print("4. Salir del Sistema")
    opc = int(input("Seleccione 1 de las 3 opciones: "))
        
    if opc == 1:
        n = int(input("Ingrese cuántos productos compró: "))
        while i <= n:
            precio = float(input("Ingrese el precio del producto " , i , ": "))
            suma = suma + precio
            i = i + 1
            if suma < 50:
                total_cancelar = suma
            elif 50 <= suma <= 99:
                desc = suma * 0.05
                total_cancelar = suma - desc
            elif 100 <= suma <= 149:
                desc = suma * 0.10
                total_cancelar = suma - desc
            elif 150 <= suma <= 199:
                desc = suma * 0.15
                total_cancelar = suma - desc
            elif 200 <= suma <= 249:
                desc = suma * 0.20
                total_cancelar = suma - desc
                
            print("El total a cancelar es:", total_cancelar)

    elif opc == 2:
        vent = float(input("Ingrese cuánto vendió semanalmente: "))
        if vent >= 1000:
            suel_tot = 450 + 100
            print("Usted obtuvo un bono, su sueldo total es: ", suel_tot)
        else:
            suel_tot = 450
            print("Usted no obtuvo bono, su sueldo total es: ", suel_tot)

    elif opc == 3:
        i = 1
        resp = input("¿Desea ingresar algún producto? (SI-NO): ")
        if resp.upper() == "SI":
            n = int(input("¿Cuántas veces desea ingresar productos?: "))
            while i <= n:
                nom_prod = input("Ingrese uno de los siguientes productos (Leche, Atún, Huevos, Papel higiénico, Alcohol, Curitas, Gasas, Sal, Café, Arroz): ")
                cant_pro = int(input("Ingrese el número de existencias del producto: "))
                if nom_prod.upper() == "LECHE":
                    exis_leche = exis_leche + cant_pro
                elif nom_prod.upper() == "ATUN":
                    exis_atun = exis_atun + cant_pro
                elif nom_prod.upper() == "HUEVOS":
                    exis_huevos = exis_huevos + cant_pro
                elif nom_prod.upper() == "PAPEL":
                    exis_papel = exis_papel + cant_pro
                elif nom_prod.upper() == "ALCOHOL":
                    exis_alcohol = exis_alcohol + cant_pro
                elif nom_prod.upper() == "CURITAS":
                    exis_curitas = exis_curitas + cant_pro
                elif nom_prod.upper() == "GASAS":
                    exis_gasas = exis_gasas + cant_pro
                elif nom_prod.upper() == "SAL":
                    exis_sal = exis_sal + cant_pro
                elif nom_prod.upper() == "CAFE":
                    exis_cafe = exis_cafe + cant_pro
                elif nom_prod.upper() == "ARROZ":
                    exis_arroz = exis_arroz + cant_pro
                else:
                    print("Error al ingresar producto, inténtelo de nuevo")
                i = i + 1
                print("Productos ingresados con éxito")
            else:
                print("Usted no ha querido ingresar algún producto")
                
            print("\nEl Inventario de productos es:\n")
            print("Leche: ", exis_leche)
            print("Atun: ", exis_atun)
            print("Huevos: ", exis_huevos)
            print("Papel Higiénico: ", exis_papel)
            print("Alcohol: ", exis_alcohol)
            print("Curitas: ", exis_curitas)
            print("Gasas: ", exis_gasas)
            print("Sal: ", exis_sal)
            print("Cafe: ", exis_cafe)
            print("Arroz: ", exis_arroz)
        else:
            print("Opción no válida")
    elif opc == 4:
        print("SALIENDO DEL SISTEMA")
        raise SystemExit
    else:
        print("Opción no válida")
        raise SystemExit


