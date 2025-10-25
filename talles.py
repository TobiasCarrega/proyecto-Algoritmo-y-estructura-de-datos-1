"""
-----------------------------------------------------------------------------------------------
Título: Carga de datos de Talles
Fecha: 2025.10.15
Autor:  Equipo 8 
Descripción: Lee los datos del archivo talles.txt y los convierte en un diccionario.
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

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
    return talles
