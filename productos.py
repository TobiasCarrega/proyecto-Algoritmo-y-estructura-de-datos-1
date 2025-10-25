"""
-----------------------------------------------------------------------------------------------
Título: Gestión de Clientes
Fecha: 2025.10.15
Autor:  Equipo 8 

Descripción:
Funciones para leer y guardar productos desde/hacia un archivo .txt

Pendientes:
- Validaciones de stock y precios
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
    productos = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    codigo = partes[0]
                    productos[codigo] = {
                        "Nombre": partes[1],
                        "Precio": float(partes[2]),
                        "Disponible": partes[3] == "True"
                    }
    return productos

def guardar_datos(file_name, productos):
    with open(file_name, "w") as f:
        for codigo, data in productos.items():
            linea = f"{codigo},{data['Nombre']},{data['Precio']},{data['Disponible']}\n"
            f.write(linea)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    productos = leer_datos("productos.txt")
    print("Productos cargados:", productos)
    # Ejemplo de alta
    codigo = "P003"
    productos[codigo] = {
        "Nombre": "Jabón Líquido",
        "Precio": 3.75,
        "Disponible": True
    }
    guardar_datos("productos.txt", productos)
    print("Productos guardados correctamente.")

if __name__ == "__main__":
    main()
