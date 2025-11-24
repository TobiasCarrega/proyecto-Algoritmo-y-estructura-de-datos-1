#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time   # Mantenemos time por consistencia general del proyecto


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# ---------------------------
# Utilidades
# ---------------------------

def listar_productos_en_stock(accesorios: dict):
    """
    Muestra los productos activos con stock mayor a 0.
    Incluye código, nombre, stock y precio diario.
    """
    print(">>> LISTADO DE PRODUCTOS EN STOCK")
    encabezado = f"{'CÓDIGO':8} {'NOMBRE':30} {'STOCK':6} {'PRECIO/DIARIO':12}"
    print(encabezado)
    print("-" * len(encabezado))

    for codigo, p in accesorios.items():
        if p.get("Activo", False) and p.get("Stock", 0) > 0:
            print(f"{codigo:8} {p.get('Nombre','')[:30]:30} "
                  f"{str(p.get('Stock')):6} {str(p.get('PrecioDiario')):12}")

    print("-" * len(encabezado))


def listar_perdidos_rotos(accesorios: dict):
    """
    Lista los productos que tienen unidades perdidas o rotas.
    """
    print(">>> LISTADO DE ÍTEMS PERDIDOS / ROTOS")
    encabezado = f"{'CÓDIGO':8} {'NOMBRE':30} {'PERDIDOS/ROTOS':15}"
    print(encabezado)
    print("-" * len(encabezado))

    for codigo, p in accesorios.items():
        if p.get("PerdidosRotura", 0) > 0:
            print(f"{codigo:8} {p.get('Nombre','')[:30]:30} "
                  f"{str(p.get('PerdidosRotura')):15}")

    print("-" * len(encabezado))


def listar_talles_producto(accesorios: dict):
    """
    Muestra los talles disponibles para cada accesorio.
    Los talles están almacenados como un diccionario {talle: True}.
    """
    print(">>> LISTADO DE TALLES POR PRODUCTO")
    for codigo, p in accesorios.items():
        if p.get("Activo", False):
            talles = ", ".join(p.get("Talles", {}).keys())
            print(f"{codigo} - {p.get('Nombre')}: {talles}")


# ---------------------------
# Gestión de Accesorios
# ---------------------------

def alta_accesorio(accesorios: dict):
    """
    Da de alta un nuevo accesorio.
    Registra: nombre, precio diario, stock inicial y talles asociados.
    """
    print(">>> ALTA ACCESORIO")
    listar_productos_en_stock(accesorios)

    codigo = input("Código producto (ej: P012): ").strip().upper()
    if codigo == "" or codigo in accesorios:
        print("Código inválido o ya existe.")
        return accesorios

    nombre = input("Nombre del accesorio: ").strip()

    precio_raw = input("Precio diario: ").strip()
    if not precio_raw.isdigit():
        print("Precio inválido.")
        return accesorios
    precio = int(precio_raw)

    stock_raw = input("Stock inicial: ").strip()
    if not stock_raw.isdigit():
        print("Stock inválido.")
        return accesorios
    stock = int(stock_raw)

    talles_raw = input("Talles disponibles (separados por coma): ").strip()
    talles = {t.strip(): True for t in talles_raw.split(",") if t.strip()}

    accesorios[codigo] = {
        "Nombre": nombre,
        "PrecioDiario": precio,
        "Stock": stock,
        "PerdidosRotura": 0,
        "Talles": talles,
        "Activo": True
    }

    print(f"Accesorio {codigo} cargado correctamente.")
    return accesorios


def modificar_accesorio(accesorios: dict):
    """
    Modifica un accesorio existente.
    Se pueden actualizar: nombre, precio y talles.
    """
    print(">>> MODIFICAR ACCESORIO")
    listar_productos_en_stock(accesorios)

    codigo = input("Código producto a modificar: ").strip().upper()
    if codigo not in accesorios:
        print("Producto no encontrado.")
        return accesorios

    prod = accesorios[codigo]

    nuevo_nombre = input(f"Nombre actual ({prod['Nombre']}): ").strip()
    if nuevo_nombre != "":
        prod["Nombre"] = nuevo_nombre

    nuevo_precio = input(f"Precio diario actual ({prod['PrecioDiario']}): ").strip()
    if nuevo_precio.isdigit():
        prod["PrecioDiario"] = int(nuevo_precio)

    talles_raw = input(f"Nuevos talles (coma sep) – ENTER mantiene actuales: ").strip()
    if talles_raw != "":
        prod["Talles"] = {t.strip(): True for t in talles_raw.split(",") if t.strip()}

    accesorios[codigo] = prod
    print(f"Producto {codigo} modificado.")
    return accesorios


def baja_logica_accesorio(accesorios: dict):
    """
    Da de baja un accesorio marcándolo como inactivo.
    No se elimina del sistema.
    """
    print(">>> BAJA LÓGICA ACCESORIO")
    codigo = input("Código producto a dar de baja: ").strip().upper()

    if codigo not in accesorios:
        print("Producto no encontrado.")
        return accesorios

    accesorios[codigo]["Activo"] = False
    print(f"Producto {codigo} marcado como inactivo.")
    return accesorios
