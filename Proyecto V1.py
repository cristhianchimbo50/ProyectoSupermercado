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

while intent < 3 and ses == 0:
    usu = input('Ingrese el usuario: ')
    cont = input('Ingrese la contraseña: ')
    
    if usu == 'tienda':
        if cont == 'T2024':
            print('**Bienvenidos al Sistema**')
            ses = 1
            print('**Bienvenidos al siguiente menú**')
            print('1. Visualizar el total a cancelar')
            print('2. Visualizar el bono de los empleados')
            print('**Inventario del Supermercado**')
            print('Bienvenidos al siguiente menú')
            print('3. Agregar productos y muestra el inventario')
            opc = int(input('Seleccione 1 de las 3 opciones: '))
            
            if opc == 1:
                n = int(input('Ingrese cuántos productos compró: '))
                while i <= n:
                    precio = float(input(f'Ingrese el precio del producto {i}: '))
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
                print(f'El total a cancelar es: {total_cancelar}')

            elif opc == 2:
                vent = float(input('Ingrese cuánto vendió semanalmente: '))
                if vent >= 1000:
                    suel_tot = 450 + 100
                    print(f'Usted obtuvo un bono, su sueldo total es: {suel_tot}')
                else:
                    suel_tot = 450
                    print(f'Usted no obtuvo bono, su sueldo total es: {suel_tot}')

            elif opc == 3:
                i = 1
                resp = input('¿Desea ingresar algún producto? (SI-NO): ')
                if resp.upper() == "SI":
                    n = int(input('¿Cuántas veces desea ingresar productos?: '))
                    while i <= n:
                        nom_prod = input('Ingrese uno de los siguientes productos (Leche, Atún, Huevos, Papel higiénico, Alcohol, Curitas, Gasas, Sal, Café, Arroz): ')
                        cant_pro = int(input('Ingrese el número de existencias del producto: '))
                        if nom_prod == "Leche":
                            exis_leche = exis_leche + cant_pro
                        elif nom_prod == "Atun":
                            exis_atun = exis_atun + cant_pro
                        elif nom_prod == "Huevos":
                            exis_huevos = exis_huevos + cant_pro
                        elif nom_prod == "Papel":
                            exis_papel = exis_papel + cant_pro
                        elif nom_prod == "Alcohol":
                            exis_alcohol = exis_alcohol + cant_pro
                        elif nom_prod == "Curitas":
                            exis_curitas = exis_curitas + cant_pro
                        elif nom_prod == "Gasas":
                            exis_gasas = exis_gasas + cant_pro
                        elif nom_prod == "Sal":
                            exis_sal = exis_sal + cant_pro
                        elif nom_prod == "Cafe":
                            exis_cafe = exis_cafe + cant_pro
                        elif nom_prod == "Arroz":
                            exis_arroz = exis_arroz + cant_pro

                        else:
                            print("Error al ingresar producto, inténtelo de nuevo")
                        i = i + 1
                    print("Productos ingresados con éxito")
                else:
                    print("Usted no ha querido ingresar algún producto")
                    
                print("El Inventario de productos es:")
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

        else:
            print('La contraseña es incorrecta')
            intent += 1

    else:
        print('El usuario es incorrecto')
        intent += 1

if intent == 3:
    print('Usuario bloqueado, utilizó 3 intentos')
