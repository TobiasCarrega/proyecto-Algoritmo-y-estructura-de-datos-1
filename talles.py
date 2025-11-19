<<<<<<< Updated upstream
"""
-----------------------------------------------------------------------------------------------
Título: Carga de datos de Talles
Fecha: 2025.10.15
Autor:  Equipo 8 
Descripción: Lee los datos del archivo talles.txt y los convierte en un diccionario.
-----------------------------------------------------------------------------------------------
"""
=======
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time    # Se mantiene por consistencia general, aunque no es estrictamente necesario

>>>>>>> Stashed changes

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

<<<<<<< Updated upstream
def cargar_talles(ruta_archivo):
    talles = {}
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            codigo, nombre, equivalencias_str, activo = linea.split(",")
            equivalencias = equivalencias_str.split("|") if equivalencias_str else []
            talles[codigo] = {
                "Nombre": nombre,
                "Equivalencias": {eq: True for eq in equivalencias},
                "Activo": activo == "True"
            }
=======
# ---------------------------
# Utilidades
# ---------------------------

def listar_talles_activos(talles: dict):
    """
    Muestra todos los talles cuyo estado sea Activo = True.
    También imprime sus equivalencias.
    """
    print(">>> LISTADO DE TALLES ACTIVOS")
    encabezado = f"{'CÓDIGO':8} {'NOMBRE':15} {'EQUIVALENCIAS'}"
    print(encabezado)
    print("-" * len(encabezado))

    for codigo, t in talles.items():
        if t.get("Activo", False):
            equivalencias = ", ".join(t.get("Equivalencias", {}).keys())
            print(f"{codigo:8} {t.get('Nombre','')[:15]:15} {equivalencias}")

    print("-" * len(encabezado))


# ---------------------------
# Gestión de Talles
# ---------------------------

def alta_talle(talles: dict):
    """
    Da de alta un nuevo talle.
    Registra:
        - código (ej: T011)
        - nombre del talle (S, M, L…)
        - equivalencias (diccionario con números u otros talles)
    """
    print(">>> ALTA TALLE")

    codigo = input("Código talle (ej: T011): ").strip().upper()
    if codigo == "" or codigo in talles:
        print("Código inválido o ya existente.")
        return talles

    nombre = input("Nombre del talle (ej: S, M, L): ").strip()
    if nombre == "":
        print("Nombre inválido.")
        return talles

    equivalencias_raw = input("Equivalencias (separadas por coma): ").strip()
    equivalencias = {
        e.strip(): True for e in equivalencias_raw.split(",") if e.strip()
    }

    talles[codigo] = {
        "Nombre": nombre,
        "Equivalencias": equivalencias,
        "Activo": True
    }

    print(f"Talle {codigo} dado de alta correctamente.")
    return talles


def modificar_talle(talles: dict, accesorios: dict):
    """
    Modifica el nombre y/o equivalencias de un talle ya existente.
    Se debe ingresar el código del talle.
    """
    print(">>> MODIFICAR TALLE")
    
    listar_talles_activos(talles)

    codigo = input("Código del talle a modificar: ").strip().upper()
    if codigo not in talles:
        print("Talle no encontrado.")
        return talles

    t = talles[codigo]

    # Modificar nombre
    nuevo_nombre = input(f"Nombre actual ({t['Nombre']}): ").strip()
    if nuevo_nombre != "":
        t["Nombre"] = nuevo_nombre

    # Modificar equivalencias
    equivalencias_raw = input(
        f"Nuevas equivalencias (coma sep) – ENTER mantiene actuales: "
    ).strip()

    if equivalencias_raw != "":
        t["Equivalencias"] = {
            e.strip(): True for e in equivalencias_raw.split(",") if e.strip()
        }

    talles[codigo] = t
    print(f"Talle {codigo} modificado correctamente.")
    return talles


def baja_logica_talle(talles: dict):
    """
    Baja lógica de un talle: se marca como inactivo,
    pero no se elimina del diccionario original.
    """
    print(">>> BAJA LÓGICA TALLE")

    codigo = input("Código del talle a dar de baja: ").strip().upper()
    if codigo not in talles:
        print("Talle no encontrado.")
        return talles

    talles[codigo]["Activo"] = False
    print(f"Talle {codigo} marcado como inactivo.")
>>>>>>> Stashed changes
    return talles
