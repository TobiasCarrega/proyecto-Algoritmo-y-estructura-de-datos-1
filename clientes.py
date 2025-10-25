"""
-----------------------------------------------------------------------------------------------
Título: Gestión de Clientes
Fecha: 24/10/2025
Autor: Martina Ortega

Descripción:
Funciones para leer y guardar clientes desde/hacia un archivo .txt

Pendientes:
- Validaciones más complejas (emails, teléfonos)
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
# Ninguno aparte de built-ins
import os

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def leer_datos(file_name):
    """
    Lee los clientes desde un archivo .txt
    """
    clientes = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    codigo = partes[0]
                    telefonos = {t: True for t in partes[5].split("|") if t}
                    clientes[codigo] = {
                        "Nombre": partes[1],
                        "Edad": int(partes[2]),
                        "DNI": partes[3],
                        "Email": partes[4],
                        "Telefonos": telefonos,
                        "Activo": partes[6] == "True"
                    }
    return clientes

def guardar_datos(file_name, clientes):
    """
    Guarda los clientes en un archivo .txt
    """
    with open(file_name, "w") as f:
        for codigo, data in clientes.items():
            telefonos = "|".join(data["Telefonos"].keys())
            linea = f"{codigo},{data['Nombre']},{data['Edad']},{data['DNI']},{data['Email']},{telefonos},{data['Activo']}\n"
            f.write(linea)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    clientes = leer_datos("clientes.txt")
    
    # Ejemplo de alta de cliente
    codigo = "C003"
    clientes[codigo] = {
        "Nombre": "Luis Martinez",
        "Edad": 28,
        "DNI": "23456789",
        "Email": "lmartinez@mail.com",
        "Telefonos": {"6677889900": True},
        "Activo": True
    }
    
    guardar_datos("clientes.txt", clientes)
    print("Clientes guardados correctamente.")

# Punto de entrada al programa
if __name__ == "__main__":
    main()

