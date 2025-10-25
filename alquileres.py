"""
-----------------------------------------------------------------------------------------------
Título: Carga de datos de Alquileres
Fecha: 2025-10-24
Autor: Martina Ortega
Descripción: Lee los datos del archivo alquileres.txt y los convierte en un diccionario
             anidado por año.
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def cargar_alquileres(ruta_archivo):
    alquileres = {}
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            anio, codigo, fecha, cliente, producto, cantidad, precio_unit, total = linea.split(",")
            if anio not in alquileres:
                alquileres[anio] = {}
            alquileres[anio][codigo] = {
                "FechaHora": fecha,
                "Cliente": cliente,
                "Producto": producto,
                "Cantidad": int(cantidad),
                "PrecioUnit": float(precio_unit),
                "Total": float(total)
            }
    return alquileres
