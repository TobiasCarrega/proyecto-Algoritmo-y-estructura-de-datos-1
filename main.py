"""
-----------------------------------------------------------------------------------------------
Título: Entrega1 - Sistema de Alquiler de Accesorios para Esquí (versión inicial)
Fecha: 2025.10.15
Autor: Equipo 8  (plantilla inicial)
Descripción:
    Estructura inicial del programa: 3 entidades maestras (clientes, accesorios, talles),
    una entidad de transacciones (alquileres) y menú multinivel con funciones separadas.
Pendientes:
    - Completar validaciones particulares y lógica de stock/descuentos
    - Implementar informes detallados (resúmenes mensuales/anuales)
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
<<<<<<< Updated upstream
import time  # permitido en el enunciado para obtener fecha/hora
from clientes import cargar_clientes
from accesorios import cargar_accesorios
from productos import cargar_productos
from talles import cargar_talles
from alquileres import cargar_alquileres
=======
import json

# Importación de los módulos del sistema
from clientes import alta_cliente, modificar_cliente, baja_logica_cliente, listar_clientes_activos
from accesorios import alta_accesorio, modificar_accesorio, baja_logica_accesorio, listar_accesorios_activos
from talles import alta_talle, modificar_talle, baja_logica_talle, listar_talles_activos
from alquileres import registrar_alquiler
from informes import (
    listar_alquileres_mes_actual,
    informe_resumen_anual,
    informe_libre_eleccion,
    informe_stock_resumen
)


>>>>>>> Stashed changes
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
# def alta_cliente(clientes):
#     codigo = f"C{len(clientes) + 1:03d}"
#     nombre = input("Nombre y Apellido: ")
#     edad = int(input("Edad: "))
#     dni = input("DNI: ")
#     email = input("Email: ")
#     telefono = input("Teléfono: ")
#     clientes[codigo] = {
#         "Nombre": nombre,
#         "Edad": edad,
#         "DNI": dni,
#         "Email": email,
#         "Telefonos": {telefono: True},
#         "Activo": True
#     }
#     print(f"Cliente {codigo} agregado correctamente.")
#     return clientes
# ---------------------------
# Archivo JSON - Utilidades
# ---------------------------

def cargar_archivo(ruta: str):
    """
    Carga un archivo JSON y devuelve su contenido.
    Si no existe, devuelve un diccionario vacío.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def guardar_archivo(ruta: str, data: dict):
    """
    Guarda un diccionario en un archivo JSON.
    """
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


#----------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
#----------------------------------------------------------------------------------------------

def main():
<<<<<<< Updated upstream
    #Cargar los datos desde los archivos .txt
    clientes = cargar_clientes("clientes.txt")
    accesorios = cargar_accesorios("accesorios.txt")
    productos = cargar_productos("productos.txt")
    talles = cargar_talles("talles.txt")
    alquileres = cargar_alquileres("alquileres.txt")

    print(">>> Sistema de alquiler de esquí iniciado correctamente.\n")
    print(f"Clientes cargados: {len(clientes)}")
    print(f"Accesorios cargados: {len(accesorios)}")
    print(f"Productos cargados: {len(productos)}")
    print(f"Talles cargados: {len(talles)}")
    print(f"Alquileres cargados: {len(alquileres)}\n")

    print("Datos cargados correctamente. (Próximo paso: menú de opciones)")

    #Guarda los datos actualizados al salir del sistema 
    guardar_clientes("clientes.txt", clientes)
    guardar_accesorios("accesorios.txt", accesorios)
    guardar_productos("productos.txt", productos)
    guardar_talles("talles.txt", talles)
    guardar_alquileres("alquileres.txt", alquileres)

    print("\nCambios guardados correctamente en los archivos.")
=======

    # ---------------------------
    # Carga inicial de archivos
    # ---------------------------
    clientes = cargar_archivo("clientes.json")
    accesorios = cargar_archivo("accesorios.json")
    talles = cargar_archivo("talles.json")
    alquileres = cargar_archivo("alquileres.json")

    while True:
        print("\n===================================")
        print("       SISTEMA DE ALQUILERES")
        print("===================================")
        print("1) Gestión de Clientes")
        print("2) Gestión de Accesorios")
        print("3) Gestión de Talles")
        print("4) Registrar Alquiler")
        print("5) Informes")
        print("6) Guardar y Salir")
        print("===================================")

        opcion = input("Seleccione opción: ").strip()
>>>>>>> Stashed changes

        # ---------------------------
        # MENÚ CLIENTES
        # ---------------------------
        if opcion == "1":
            while True:
                print("\n--- GESTIÓN DE CLIENTES ---")
                print("1) Alta cliente")
                print("2) Modificar cliente")
                print("3) Baja lógica cliente")
                print("4) Listar clientes activos")
                print("5) Volver")
                sub = input("Seleccione opción: ").strip()

                if sub == "1":
                    alta_cliente(clientes)
                elif sub == "2":
                    modificar_cliente(clientes)
                elif sub == "3":
                    baja_logica_cliente(clientes)
                elif sub == "4":
                    listar_clientes_activos(clientes)
                elif sub == "5":
                    break
                else:
                    print("Opción inválida.")

        # ---------------------------
        # MENÚ ACCESORIOS
        # ---------------------------
        elif opcion == "2":
            while True:
                print("\n--- GESTIÓN DE ACCESORIOS ---")
                print("1) Alta accesorio")
                print("2) Modificar accesorio")
                print("3) Baja lógica accesorio")
                print("4) Listar accesorios activos")
                print("5) Volver")
                sub = input("Seleccione opción: ").strip()

                if sub == "1":
                    alta_accesorio(accesorios)
                elif sub == "2":
                    modificar_accesorio(accesorios)
                elif sub == "3":
                    baja_logica_accesorio(accesorios)
                elif sub == "4":
                    listar_accesorios_activos(accesorios)
                elif sub == "5":
                    break
                else:
                    print("Opción inválida.")

        # ---------------------------
        # MENÚ TALLES
        # ---------------------------
        elif opcion == "3":
            while True:
                print("\n--- GESTIÓN DE TALLES ---")
                print("1) Alta talle")
                print("2) Modificar talle")
                print("3) Baja lógica talle")
                print("4) Listar talles activos")
                print("5) Volver")
                sub = input("Seleccione opción: ").strip()

                if sub == "1":
                    alta_talle(talles)
                elif sub == "2":
                    modificar_talle(talles, accesorios)
                elif sub == "3":
                    baja_logica_talle(talles)
                elif sub == "4":
                    listar_talles_activos(talles)
                elif sub == "5":
                    break
                else:
                    print("Opción inválida.")

        # ---------------------------
        # REGISTRAR ALQUILER
        # ---------------------------
        elif opcion == "4":
            registrar_alquiler(alquileres, clientes, accesorios)

        # ---------------------------
        # MENÚ INFORMES
        # ---------------------------
        elif opcion == "5":
            while True:
                print("\n--- INFORMES ---")
                print("1) Alquileres del mes actual")
                print("2) Resumen anual de alquileres")
                print("3) Informe libre elección")
                print("4) Resumen de stock")
                print("5) Volver")
                sub = input("Seleccione opción: ").strip()

                if sub == "1":
                    listar_alquileres_mes_actual(alquileres, clientes, accesorios)
                elif sub == "2":
                    informe_resumen_anual(alquileres, clientes, accesorios)
                elif sub == "3":
                    informe_libre_eleccion(alquileres, clientes, accesorios)
                elif sub == "4":
                    informe_stock_resumen(accesorios)
                elif sub == "5":
                    break
                else:
                    print("Opción inválida.")

        # ---------------------------
        # GUARDAR Y SALIR
        # ---------------------------
        elif opcion == "6":
            print("Guardando archivos...")

            guardar_archivo("clientes.json", clientes)
            guardar_archivo("accesorios.json", accesorios)
            guardar_archivo("talles.json", talles)
            guardar_archivo("alquileres.json", alquileres)

            print("Datos guardados correctamente. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


#----------------------------------------------------------------------------------------------
# EJECUCIÓN
#----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
