"""
-----------------------------------------------------------------------------------------------
Título: Entrega1 - Sistema de Alquiler de Accesorios para Esquí (versión inicial)
Fecha: 2025.11.24
Autor: Equipo 08 - Tobias Carrega
                Lucia Zuccarello
                López Mateo
                Hernández Nicolás
                Ortega Torres Martina
Descripción: main.py - Programa principal que integra todos los módulos del sistema de alquiler de accesorios para esquí."""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

import json

# Importación de los módulos del sistema
from clientes import (
    alta_cliente, modificar_cliente, baja_logica_cliente, listar_clientes_activos
)
from accesorios import (
    alta_accesorio, modificar_accesorio, baja_logica_accesorio, listar_productos_en_stock
)
from talles import (
    alta_talle, modificar_talle, baja_logica_talle, listar_talles_activos
)
from alquileres import registrar_alquiler
from informes import (
    listar_alquileres_mes_actual,
    informe_anual_por_cliente,
    informe_recaudacion_anual,
    informe_stock_total
)


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# ---------------------------
# Utilidades JSON
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
                print("4) Listar productos en stock")
                print("5) Volver")
                sub = input("Seleccione opción: ").strip()

                if sub == "1":
                    alta_accesorio(accesorios)
                elif sub == "2":
                    modificar_accesorio(accesorios)
                elif sub == "3":
                    baja_logica_accesorio(accesorios)
                elif sub == "4":
                    listar_productos_en_stock(accesorios)
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
                print("2) Informe ANUAL por cliente")
                print("3) Informe ANUAL de recaudación")
                print("4) Resumen de stock total")
                print("5) Volver")
                sub = input("Seleccione opción: ").strip()

                if sub == "1":
                    listar_alquileres_mes_actual(alquileres, clientes, accesorios)

                elif sub == "2":
                    anio = input("Ingrese año (AAAA): ").strip()
                    informe_anual_por_cliente(alquileres, clientes, anio)

                elif sub == "3":
                    anio = input("Ingrese año (AAAA): ").strip()
                    informe_recaudacion_anual(alquileres, anio)

                elif sub == "4":
                    informe_stock_total(accesorios)

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
