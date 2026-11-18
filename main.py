
from equipos import (
    registrar_equipo,
    listar_equipos,
    contar_por_categoria
)

from prestamos import (
    registrar_prestamo,
    devolver_equipo
)


def mostrar_menu():
    print("\n================================")
    print(" SISTEMA DE PRESTAMOS LABTECH")
    print("================================")
    print("1. Registrar equipo")
    print("2. Registrar prestamo")
    print("3. Devolver equipo")
    print("4. Listar equipos")
    print("5. Consultar por categoria")
    print("6. Salir")
    print("================================")


def main():

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_equipo()

        elif opcion == "2":
            registrar_prestamo()

        elif opcion == "3":
            devolver_equipo()

        elif opcion == "4":
            listar_equipos()

        elif opcion == "5":
            contar_por_categoria()

        elif opcion == "6":
            print("Gracias por utilizar LabTech.")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    main()
