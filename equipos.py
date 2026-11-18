
equipos = []

def validar_texto(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato:
            return dato

        print("Error: este campo no puede estar vacio.")


def registrar_equipo():
    print("\n--- REGISTRAR EQUIPO ---")

    codigo = validar_texto("Codigo del equipo: ")

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            print("Error: el codigo ya existe.")
            return

    nombre = validar_texto("Nombre del equipo: ")
    categoria = validar_texto("Categoria: ")

    nuevo_equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "disponible": True
    }

    equipos.append(nuevo_equipo)

    print("Equipo registrado correctamente.")


def listar_equipos():
    print("\n--- LISTA DE EQUIPOS ---")

    if not equipos:
        print("No hay equipos registrados.")
        return

    for equipo in equipos:
        estado = "Disponible" if equipo["disponible"] else "Prestado"

        print(
            f'{equipo["codigo"]} | '
            f'{equipo["nombre"]} | '
            f'{equipo["categoria"]} | {estado}'
        )


def contar_por_categoria():
    categoria = validar_texto("Ingrese la categoria: ").lower()

    cantidad = sum(
        1 for equipo in equipos
        if equipo["categoria"].lower() == categoria
        and equipo["disponible"]
    )

    print(f"Equipos disponibles en {categoria}: {cantidad}")
