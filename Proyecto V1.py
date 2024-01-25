#Inicio de Sesion#
while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == 'usuario1' and contrasena == 'contrasena1':
        print("Inicio de sesión exitoso. ¡Bienvenido, usuario1!")
        break
    elif usuario == 'usuario2' and contrasena == 'contrasena2':
        print("Inicio de sesión exitoso. ¡Bienvenido, usuario2!")
        break
    elif usuario == 'usuario3' and contrasena == 'contrasena3':
        print("Inicio de sesión exitoso. ¡Bienvenido, usuario3!")
        break
    else:
        print("Nombre de usuario o contraseña incorrectos. Inténtelo nuevamente.")
