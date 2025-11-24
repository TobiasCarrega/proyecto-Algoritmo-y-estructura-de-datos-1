#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time   # Módulo estándar permitido para manejo general de tiempo


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# ---------------------------
# Utilidades
# ---------------------------

def listar_clientes_activos(clientes: dict):
    """
    Muestra en pantalla todos los clientes con estado Activo = True.
    Incluye código, nombre, edad y teléfonos.
    """
    print(">>> LISTADO DE CLIENTES ACTIVOS")
    encabezado = f"{'CÓDIGO':8} {'NOMBRE':30} {'EDAD':4} {'TELÉFONOS'}"
    print(encabezado)
    print("-" * len(encabezado))

    for codigo, datos in clientes.items():
        if datos.get("Activo", False):
            telefonos = ", ".join(datos.get("Telefonos", {}).keys())
            print(f"{codigo:8} {datos.get('Nombre','')[:30]:30} "
                  f"{str(datos.get('Edad','')):4} {telefonos}")

    print("-" * len(encabezado))


# ---------------------------
# Gestion de Clientes
# ---------------------------

def alta_cliente(clientes: dict):
    """
    Da de alta un nuevo cliente.
    Asigna código automático con formato C###.
    Guarda teléfonos como un diccionario {telefono: True}.
    """
    print(">>> ALTA CLIENTE")

    # generar el próximo código automáticamente
    if not clientes:
        next_n = 1
    else:
        ultima_clave = list(clientes.keys())[-1]  # ejemplo "C012"
        numero_str = ultima_clave[1:]            # obtiene "012"
        next_n = int(numero_str) + 1 if numero_str.isdigit() else 1

    codigo = f"C{next_n:03d}"
    print(f"Código asignado: {codigo}")

    # cargar datos del cliente
    nombre = input("Nombre y Apellido: ").strip()
    if nombre == "":
        print("Nombre inválido.")
        return clientes

    edad_str = input("Edad: ").strip()
    if not edad_str.isdigit() or int(edad_str) < 18:
        print("No se permiten menores de edad.")
        return clientes
    edad = int(edad_str)

    telefonos_raw = input("Teléfonos (coma separados): ").strip()
    telefonos = {
        t.strip(): True for t in telefonos_raw.split(",") if t.strip()
    }

    clientes[codigo] = {
        "Nombre": nombre,
        "Edad": edad,
        "DNI": input("DNI (opcional): ").strip(),
        "Email": input("Email (opcional): ").strip(),
        "Telefonos": telefonos,
        "Activo": True
    }

    print(f"Cliente {codigo} dado de alta.")
    return clientes


def modificar_cliente(clientes: dict):
    """
    Permite modificar el nombre, DNI o teléfonos de un cliente.
    Se acepta dejar un campo vacío para mantener el valor actual.
    """
    print(">>> MODIFICAR CLIENTE")
    listar_clientes_activos(clientes)

    codigo = input("Código cliente a modificar: ").strip().upper()
    if codigo not in clientes:
        print("Cliente no encontrado.")
        return clientes

    cli = clientes[codigo]

    # modificar nombre
    nombre = input(f"Nombre actual ({cli['Nombre']}): ").strip()
    if nombre != "":
        cli["Nombre"] = nombre

    # modificar DNI
    dni = input(f"DNI actual ({cli.get('DNI','')}): ").strip()
    if dni != "":
        cli["DNI"] = dni

    # modificar teléfonos
    telefonos_raw = input(f"Nuevos teléfonos (coma sep) – ENTER mantiene actuales: ").strip()
    if telefonos_raw != "":
        cli["Telefonos"] = {
            t.strip(): True for t in telefonos_raw.split(",") if t.strip()
        }

    clientes[codigo] = cli
    print(f"Cliente {codigo} modificado.")
    return clientes


def baja_logica_cliente(clientes: dict):
    """
    Marca un cliente como inactivo sin eliminarlo del sistema.
    """
    print(">>> BAJA LÓGICA CLIENTE")
    codigo = input("Código cliente: ").strip().upper()

    if codigo not in clientes:
        print("Cliente no encontrado.")
        return clientes

    clientes[codigo]["Activo"] = False
    print(f"Cliente {codigo} marcado como inactivo.")
    return clientes
