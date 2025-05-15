
USUARIO_VALIDO = "admin"
CONTRASENA_VALIDA = "1234"

def iniciar_sesion():
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        # Defecto 1 (introducido intencionalmente):
        # ERROR: El programador comete un error al escribir el condicional mal.
        # DEFECTO: En vez de usar '==' para ambas comparaciones, solo compara la contraseña correctamente.
        # FALLA: Si el usuario escribe correctamente el nombre de usuario pero no se evalúa, se produce un comportamiento incorrecto.
        # Línea defectuosa:
        # if usuario and contrasena == CONTRASENA_VALIDA:
        # Explicación: El usuario puede acceder aun si no es igual a USUARIO_VALIDO
        if usuario and contrasena == CONTRASENA_VALIDA:
            print("Inicio de sesión exitoso.")
            return True
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

    # Defecto 2 (introducido intencionalmente):
    # ERROR: El programador comete un error de lógica al manejar el caso cuando se agotan los intentos.
    # DEFECTO: No se informa claramente que el acceso ha sido denegado después de 3 intentos fallidos.
    # FALLA: El usuario no sabe si el proceso terminó definitivamente o si puede seguir intentando.
    return False  # No se muestra mensaje de acceso denegado

iniciar_sesion()
