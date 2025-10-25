"""
-----------------------------------------------------------------------------------------------
Título: Gestión de Accesorios
Fecha: 24/10/2025
Autor: Martina Ortega

Descripción:
Funciones para leer y guardar accesorios desde/hacia un archivo .txt

Pendientes:
- Validaciones de precios y disponibilidad
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import os

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def leer_datos(file_name):
    accesorios = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    codigo = partes[0]
                    accesorios[codigo] = {
                        "Nombre": partes[1],
                        "Precio": float(partes[2]),
                        "Disponible": partes[3] == "True"
                    }
    return accesorios

def guardar_datos(file_name, accesorios):
    with open(file_name, "w") as f:
        for codigo, data in accesorios.items():
            linea = f"{codigo},{data['Nombre']},{data['Precio']},{data['Disponible']}\n"
            f.write(linea)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    accesorios = leer_datos("accesorios.txt")
    print("Accesorios cargados:", accesorios)
    # Ejemplo de alta
    codigo = "A003"
    accesorios[codigo] = {
        "Nombre": "Cargador USB",
        "Precio": 15.50,
        "Disponible": True
    }
    guardar_datos("accesorios.txt", accesorios)
    print("Accesorios guardados correctamente.")

if __name__ == "__main__":
    main()

