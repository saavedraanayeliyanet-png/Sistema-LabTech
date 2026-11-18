
from equipos import equipos, validar_texto

prestamos = []


def registrar_prestamo():
    print("\n--- REGISTRAR PRESTAMO ---")

    codigo = validar_texto("Codigo del equipo: ")

    equipo_encontrado = None

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("Error: el equipo no existe.")
        return

    if not equipo_encontrado["disponible"]:
        print("Error: el equipo ya esta prestado.")
        return

    estudiante = validar_texto("Nombre del estudiante: ")
    fecha = validar_texto("Fecha del prestamo: ")

    nuevo_prestamo = {
        "codigo": codigo,
        "estudiante": estudiante,
        "fecha": fecha,
        "devuelto": False
    }

    prestamos.append(nuevo_prestamo)
    equipo_encontrado["disponible"] = False

    print("Prestamo registrado correctamente.")


def devolver_equipo():
    print("\n--- DEVOLVER EQUIPO ---")

    codigo = validar_texto("Codigo del equipo: ")

    equipo_encontrado = None

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("Error: el equipo no existe.")
        return

    if equipo_encontrado["disponible"]:
        print("El equipo ya se encuentra disponible.")
        return

    for prestamo in prestamos:
        if prestamo["codigo"] == codigo and not prestamo["devuelto"]:
            prestamo["devuelto"] = True
            break

    equipo_encontrado["disponible"] = True

    print("Equipo devuelto correctamente.")

        