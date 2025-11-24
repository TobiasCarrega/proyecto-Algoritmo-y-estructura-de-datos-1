"""
-----------------------------------------------------------------------------------------------
Título: Entrega1 - Sistema de Alquiler de Accesorios para Esquí (versión inicial)
Fecha: 2025.10.15
Autor: Equipo 08 - Tobias Carrega
                Lucia Zuccarello
                López Mateo
                Hernández Nicolás
                Ortega Torres Martina
Descripción:
    Estructura inicial del programa: 3 entidades maestras (clientes, accesorios, talles),
    una entidad de transacciones (alquileres) y menú multinivel con funciones separadas.
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time  # permitido en el enunciado para obtener fecha/hora


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# ---------------------------
# Utilidades
# ---------------------------
def fecha_hora_actual():
    """
    Objetivo: Obtener la fecha y hora actual del sistema en formato estandarizado.
    Entrada: Ninguna.
    Salida: String con formato "AAAA.MM.DD HH:MM:SS" (ej: "2025.11.19 14:30:45").
    """
    return time.strftime("%Y.%m.%d %H:%M:%S")


def validar_entero_en_rango(texto_input: str, min_val: int, max_val: int):
    """
    Objetivo: Solicitar al usuario un entero dentro de un rango específico con validación repetida.
    Entrada: 
        - texto_input (str): Mensaje a mostrar en el input.
        - min_val (int): Valor mínimo permitido (inclusive).
        - max_val (int): Valor máximo permitido (inclusive).
    Salida: Integer validado dentro del rango [min_val, max_val].
    """
    while True:
        valor = input(texto_input).strip()
        if valor.isdigit():
            n = int(valor)
            if min_val <= n <= max_val:
                return n
        print(f"Error: ingrese un número entero entre {min_val} y {max_val}.")


def pausar():
    """
    Objetivo: Pausar la ejecución y esperar confirmación del usuario (presionar ENTER).
    Entrada: Ninguna.
    Salida: Ninguna (solo pausa la ejecución).
    """
    input("\nPresione ENTER para volver al menú.")


# ---------------------------
# CRUD CLIENTES
# ---------------------------
def alta_cliente(clientes: dict):
    """
    Objetivo: Registrar un nuevo cliente con código asignado automáticamente.
    Entrada: 
        - clientes (dict): Diccionario con los clientes existentes.
    Salida: Diccionario actualizado con el nuevo cliente agregado (código, nombre, edad, DNI, email, teléfonos).
    """
    print(">>> ALTA CLIENTE")

    if len(clientes) == 0:
        next_n = 1
    else:
        ultima_clave = list(clientes.keys())[-1]
        numero_str = ultima_clave[1:]
        if numero_str.isdigit():
            next_n = int(numero_str) + 1
        else:
            next_n = 1

    codigo = f"C{next_n:03d}"
    print(f"Código asignado: {codigo}")

    nombre = input("Nombre y Apellido: ").strip()
    if nombre == "":
        print("Nombre inválido.")
        return clientes

    edad_str = input("Edad: ").strip()
    if not edad_str.isdigit() or int(edad_str) < 18:
        print("No se permiten clientes menores a 18 años.")
        return clientes
    edad = int(edad_str)

    telefonos_raw = input("Teléfonos (separe por coma si hay más de uno): ").strip()
    telefonos = {t.strip(): True for t in telefonos_raw.split(",") if t.strip() != ""}

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
    Objetivo: Modificar datos de un cliente existente (nombre, DNI, teléfonos).
    Entrada: 
        - clientes (dict): Diccionario con los clientes existentes.
    Salida: Diccionario actualizado con los cambios realizados al cliente.
    """
    print(">>> MODIFICAR CLIENTE")
    listar_clientes_activos(clientes)
    codigo = input("Código cliente a modificar: ").strip().upper()
    if codigo not in clientes:
        print("Cliente no encontrado.")
        return clientes

    cli = clientes[codigo]
    print("Dejar vacío para mantener valor actual.")
    nombre = input(f"Nombre ({cli.get('Nombre')}): ").strip()
    if nombre != "":
        cli["Nombre"] = nombre

    dni = input(f"DNI ({cli.get('DNI')}): ").strip()
    if dni != "":
        cli["DNI"] = dni

    telefonos_raw = input(f"Teléfonos actuales {list(cli.get('Telefonos', {}).keys())}. Nuevos (coma sep): ").strip()
    if telefonos_raw != "":
        cli["Telefonos"] = {t.strip(): True for t in telefonos_raw.split(",") if t.strip() != ""}

    clientes[codigo] = cli
    print(f"Cliente {codigo} modificado.")
    return clientes


def baja_logica_cliente(clientes: dict):
    """
    Objetivo: Marcar un cliente como inactivo sin eliminar sus datos (baja lógica).
    Entrada: 
        - clientes (dict): Diccionario con los clientes existentes.
    Salida: Diccionario con el cliente marcado como inactivo (Activo = False).
    """
    print(">>> ELIMINAR (Baja lógica) CLIENTE")
    print(">>> ej:codigo de cliente: C011")
    codigo = input("Código cliente a dar de baja: ").strip().upper()
    if codigo not in clientes:
        print("Cliente no encontrado.")
        return clientes
    clientes[codigo]["Activo"] = False
    print(f"Cliente {codigo} marcado como inactivo.")
    return clientes


def listar_clientes_activos(clientes: dict):
    """
    Objetivo: Mostrar en formato tabular todos los clientes con estado Activo = True.
    Entrada: 
        - clientes (dict): Diccionario con los clientes existentes.
    Salida: Ninguna (solo visualización en pantalla).
    """
    print(">>> LISTADO DE CLIENTES ACTIVOS")
    encabezado = f"{'CÓDIGO':8} {'NOMBRE':30} {'EDAD':4} {'TELÉFONOS'}"
    print(encabezado)
    print("-" * len(encabezado))
    for codigo, datos in clientes.items():
        if datos.get("Activo", False):
            telefonos = ", ".join(datos.get("Telefonos", {}).keys())
            print(f"{codigo:8} {datos.get('Nombre','')[:30]:30} {str(datos.get('Edad','')):4} {telefonos}")
    print("-" * len(encabezado))

    # no return (solo visualización)


# ---------------------------
# CRUD ACCESORIOS / PRODUCTOS
# ---------------------------
def alta_accesorio(accesorios: dict):
    """
    Objetivo: Registrar un nuevo producto/accesorio con código definido por el usuario.
    Entrada: 
        - accesorios (dict): Diccionario con los accesorios existentes.
    Salida: Diccionario actualizado con el nuevo accesorio (código, nombre, precio, stock, talles).
    """
    print(">>> ALTA ACCESORIO")
    listar_productos_en_stock(accesorios)

    codigo = input("Código producto (ej: P011): ").strip()
    if codigo == "" or codigo in accesorios:
        print("Código inválido o ya existe.")
        return accesorios

    nombre = input("Nombre del accesorio: ").strip()
    precio_raw = input("Precio diario (sin separadores): ").strip()
    if not precio_raw.isdigit():
        print("Precio inválido.")
        return accesorios
    precio = int(precio_raw)
    stock_raw = input("Stock inicial (entero): ").strip()
    if not stock_raw.isdigit():
        print("Stock inválido.")
        return accesorios
    stock = int(stock_raw)

    talles_raw = input("Talles disponibles (separar por coma): ").strip()
    talles = {t.strip(): True for t in talles_raw.split(",") if t.strip() != ""}

    accesorios[codigo] = {
        "Nombre": nombre,
        "PrecioDiario": precio,
        "Stock": stock,
        "PerdidosRotura": 0,
        "Talles": talles,
        "Activo": True
    }
    print(f"Accesorio {codigo} cargado.")
    return accesorios


def modificar_accesorio(accesorios: dict):
    """
    Objetivo: Modificar datos de un producto existente (nombre, precio, talles).
    Entrada: 
        - accesorios (dict): Diccionario con los accesorios existentes.
    Salida: Diccionario actualizado con los cambios realizados al accesorio.
    """
    print(">>> MODIFICAR ACCESORIO")
    listar_productos_en_stock(accesorios)

    codigo = input("Código producto a modificar: ").strip()
    if codigo not in accesorios:
        print("Producto no encontrado.")
        return accesorios

    prod = accesorios[codigo]
    nombre = input(f"Nombre ({prod.get('Nombre')}): ").strip()
    if nombre != "":
        prod["Nombre"] = nombre

    precio_raw = input(f"Precio diario ({prod.get('PrecioDiario')}): ").strip()
    if precio_raw.isdigit():
        prod["PrecioDiario"] = int(precio_raw)

    talles_raw = input(f"Talles actuales {list(prod.get('Talles', {}).keys())}. Nuevos (coma sep): ").strip()
    if talles_raw != "":
        prod["Talles"] = {t.strip(): True for t in talles_raw.split(",") if t.strip() != ""}

    accesorios[codigo] = prod
    print(f"Producto {codigo} modificado.")
    return accesorios


def baja_logica_accesorio(accesorios: dict):
    """
    Objetivo: Marcar un producto como inactivo sin eliminar sus datos (baja lógica).
    Entrada: 
        - accesorios (dict): Diccionario con los accesorios existentes.
    Salida: Diccionario con el accesorio marcado como inactivo (Activo = False).
    """
    print(">>> ELIMINAR (Baja lógica) ACCESORIO")
    codigo = input("Código producto a dar de baja: ").strip()
    if codigo not in accesorios:
        print("Producto no encontrado.")
        return accesorios
    accesorios[codigo]["Activo"] = False
    print(f"Producto {codigo} marcado como inactivo.")
    return accesorios


def listar_productos_en_stock(accesorios: dict):
    """
    Objetivo: Mostrar en formato tabular los productos activos con stock disponible (> 0).
    Entrada: 
        - accesorios (dict): Diccionario con los accesorios existentes.
    Salida: Ninguna (solo visualización en pantalla).
    """
    print(">>> LISTADO DE PRODUCTOS EN STOCK")
    encabezado = f"{'CÓDIGO':8} {'NOMBRE':30} {'STOCK':6} {'PRECIO/DIARIO':12}"
    print(encabezado)
    print("-" * len(encabezado))
    for codigo, p in accesorios.items():
        if p.get("Activo", False) and p.get("Stock", 0) > 0:
            print(f"{codigo:8} {p.get('Nombre','')[:30]:30} {str(p.get('Stock')):6} {str(p.get('PrecioDiario')):12}")
    print("-" * len(encabezado))



def listar_perdidos_rotos(accesorios: dict):
    """
    Objetivo: Mostrar productos con registro de pérdida o rotura para auditoría.
    Entrada: 
        - accesorios (dict): Diccionario con los accesorios existentes.
    Salida: Ninguna (solo visualización en pantalla).
    """
    print(">>> LISTADO DE ÍTEMS PERDIDOS / ROTOS")
    encabezado = f"{'CÓDIGO':8} {'NOMBRE':30} {'PERDIDOS/ROTOS':15}"
    print(encabezado)
    print("-" * len(encabezado))
    for codigo, p in accesorios.items():
        if p.get("PerdidosRotura", 0) > 0:
            print(f"{codigo:8} {p.get('Nombre','')[:30]:30} {str(p.get('PerdidosRotura')):15}")


def listar_talles_producto(accesorios: dict):
    """
    Objetivo: Mostrar la relación entre productos y talles disponibles para cada uno.
    Entrada: 
        - accesorios (dict): Diccionario con los accesorios existentes.
    Salida: Ninguna (solo visualización en pantalla).
    """
    print(">>> LISTADO DE TALLES POR PRODUCTO")
    for codigo, p in accesorios.items():
        if p.get("Activo", False):
            print(f"{codigo} - {p.get('Nombre')}: {', '.join(p.get('Talles', {}).keys())}")


def alta_talle(talles: dict):
    """
    Objetivo: Registrar un nuevo talle con código definido por el usuario.
    Entrada: 
        - talles (dict): Diccionario con los talles existentes.
    Salida: Diccionario actualizado con el nuevo talle (código, nombre, equivalencias).
    """
    print(">>> ALTA TALLE")
    codigo = input("Código talle (ej: T011): ").strip()
    if codigo == "" or codigo in talles:
        print("Código inválido o ya existe.")
        return talles

    nombre = input("Nombre del talle (ej: S, M, L): ").strip()
    equivalencias_raw = input("Equivalencias (separar por coma): ").strip()
    equivalencias = {e.strip(): True for e in equivalencias_raw.split(",") if e.strip() != ""}

    talles[codigo] = {
        "Nombre": nombre,
        "Equivalencias": equivalencias,
        "Activo": True
    }
    print(f"Talle {codigo} dado de alta.")
    return talles


def modificar_talle(talles: dict, accesorios: dict):
    """
    Objetivo: Modificar datos de un talle existente (nombre y equivalencias).
    Entrada: 
        - talles (dict): Diccionario con los talles existentes.
        - accesorios (dict): Diccionario con accesorios (para mostrar contexto).
    Salida: Diccionario actualizado con los cambios realizados al talle.
    """
    print(">>> MODIFICAR TALLE")
    listar_productos_en_stock(accesorios)

    codigo = input("Código talle a modificar: ").strip()
    if codigo not in talles:
        print("Talle no encontrado.")
        return talles

    t = talles[codigo]
    nombre = input(f"Nombre ({t.get('Nombre')}): ").strip()
    if nombre != "":
        t["Nombre"] = nombre

    equivalencias_raw = input(f"Equivalencias actuales {list(t.get('Equivalencias', {}).keys())}. Nuevas (coma sep): ").strip()
    if equivalencias_raw != "":
        t["Equivalencias"] = {e.strip(): True for e in equivalencias_raw.split(",") if e.strip() != ""}

    talles[codigo] = t
    print(f"Talle {codigo} modificado.")
    return talles


def baja_logica_talle(talles: dict):
    """
    Objetivo: Marcar un talle como inactivo sin eliminar sus datos (baja lógica).
    Entrada: 
        - talles (dict): Diccionario con los talles existentes.
    Salida: Diccionario con el talle marcado como inactivo (Activo = False).
    """
    print(">>> ELIMINAR (Baja lógica) TALLE")
    codigo = input("Código talle a dar de baja: ").strip()
    if codigo not in talles:
        print("Talle no encontrado.")
        return talles
    talles[codigo]["Activo"] = False
    print(f"Talle {codigo} marcado como inactivo.")
    return talles


def listar_talles_activos(talles: dict):
    """
    Objetivo: Mostrar todos los talles con estado Activo = True con sus equivalencias.
    Entrada: 
        - talles (dict): Diccionario con los talles existentes.
    Salida: Ninguna (solo visualización en pantalla).
    """
    print(">>> LISTADO DE TALLES ACTIVOS")
    for codigo, t in talles.items():
        if t.get("Activo", False):
            print(f"{codigo}: {t.get('Nombre')} - Equiv: {', '.join(t.get('Equivalencias', {}).keys())}")


def registrar_alquiler(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Objetivo: Registrar una nueva transacción de alquiler validando cliente, producto y stock.
    Entrada: 
        - alquileres (dict): Diccionario de transacciones anidado por año.
        - clientes (dict): Diccionario con clientes para validación.
        - accesorios (dict): Diccionario con accesorios para validación y actualización de stock.
    Salida: Diccionario actualizado con la nueva transacción registrada (ID, fecha, cliente, producto, cantidad, total).
    """
    print(">>> REGISTRAR ALQUILER")
    anio = time.strftime("%Y")
    if anio not in alquileres:
        alquileres[anio] = {}

    next_id = f"ALQ{len(alquileres[anio]) + 1:04d}"
    codigo_cliente = input("Código cliente: ").strip().upper()
    if codigo_cliente not in clientes or not clientes[codigo_cliente].get("Activo", False):
        print("Cliente inválido o inactivo.")
        return alquileres

    codigo_producto = input("Código producto: ").strip().upper()
    if codigo_producto not in accesorios or not accesorios[codigo_producto].get("Activo", False):
        print("Producto inválido o inactivo.")
        return alquileres

    cantidad_raw = input("Cantidad a alquilar: ").strip()
    if not cantidad_raw.isdigit() or int(cantidad_raw) <= 0:
        print("Cantidad inválida.")
        return alquileres
    cantidad = int(cantidad_raw)

    if accesorios[codigo_producto].get("Stock", 0) < cantidad:
        print("Stock insuficiente.")
        return alquileres

    precio_unit = accesorios[codigo_producto].get("PrecioDiario", 0)
    total = precio_unit * cantidad

    fh = fecha_hora_actual()
    alquileres[anio][next_id] = {
        "FechaHora": fh,
        "Cliente": codigo_cliente,
        "Producto": codigo_producto,
        "Cantidad": cantidad,
        "PrecioUnit": precio_unit,
        "Total": total
    }

    accesorios[codigo_producto]["Stock"] -= cantidad

    print(f"Alquiler registrado: {next_id} - {fh} - Cliente {codigo_cliente} - Producto {codigo_producto} - Cant {cantidad}")
    return alquileres


def listar_alquileres_mes_actual(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Objetivo: Mostrar en formato tabular todos los alquileres del mes actual.
    Entrada: 
        - alquileres (dict): Diccionario de transacciones anidado por año.
        - clientes (dict): Diccionario con clientes para resolver nombres.
        - accesorios (dict): Diccionario con accesorios para resolver nombres.
    Salida: Ninguna (solo visualización en pantalla).
    """
    print(">>> LISTADO DE ALQUILERES - MES ACTUAL")
    anio = time.strftime("%Y")
    mes = time.strftime("%m")
    encabezado = f"{'Fecha/Hora':20} {'Cliente':20} {'Producto':25} {'Cant.':6} {'Unit.':10} {'Total':12}"
    print(encabezado)
    print("-" * len(encabezado))
    if anio not in alquileres:
        print("No hay operaciones en el año actual.")
        return
    for id_alq, datos in alquileres[anio].items():
        fecha = datos.get("FechaHora", "")
        if len(fecha) >= 7 and fecha[5:7] == mes:
            cliente_nombre = clientes.get(datos.get("Cliente"), {}).get("Nombre", datos.get("Cliente"))
            producto_nombre = accesorios.get(datos.get("Producto"), {}).get("Nombre", datos.get("Producto"))
            print(f"{fecha:20} {cliente_nombre[:20]:20} {producto_nombre[:25]:25} {str(datos.get('Cantidad')):6} {str(datos.get('PrecioUnit')):10} {str(datos.get('Total')):12}")


def informe_resumen_anual(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Objetivo: Mostrar un resumen anual detallado de todas las transacciones con acumuladores.
    Entrada: 
        - alquileres (dict): Diccionario de transacciones anidado por año.
        - clientes (dict): Diccionario con clientes para resolver nombres.
        - accesorios (dict): Diccionario con accesorios para resolver nombres.
    Salida: Ninguna (solo visualización en pantalla con detalles por año, cantidad de operaciones, unidades y recaudación).
    """
    print(">>> LISTADO DE ALQUILERES - ANUAL")
    encabezado = f"{'Año':4}{'ID_Alquiler':18}{'Fecha/Hora':20}{'Cliente':20}{'Producto':28}{'Cant.':10}{'Unit.':15}{'Total':12}"
    print(encabezado)
    print("-" * len(encabezado))

    for año, datos_anuales in alquileres.items():
        contador = 0
        recaudacion = 0
        unidades = 0

        for id_alq, datos in datos_anuales.items():
            fecha = datos.get("FechaHora", "")
            cliente_nombre = clientes.get(datos.get("Cliente"), {}).get("Nombre", datos.get("Cliente"))
            producto_nombre = accesorios.get(datos.get("Producto"), {}).get("Nombre", datos.get("Producto"))
            cantidad = datos.get("Cantidad", 0)
            unitario = datos.get("PrecioUnit", 0)
            total = datos.get("Total", 0)

            contador += 1
            recaudacion += total
            unidades += cantidad

            # imprimir detalle
            print(f"{año:4} {id_alq:12} {fecha:20} {cliente_nombre[:20]:20} {producto_nombre[:25]:25} {cantidad:6} {unitario:10} {total:12}")

        print("-" * len(encabezado))
        print(f">>> Total de alquileres en {año}: {contador}")
        print(f">>> Unidades alquiladas en {año}: {unidades}")
        print(f">>> Recaudación total en {año}: ${recaudacion}")
        print("=" * len(encabezado))


def informe_libre_eleccion(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Objetivo: Mostrar listado detallado de todas las transacciones con nombres resueltos.
    Entrada: 
        - alquileres (dict): Diccionario de transacciones anidado por año.
        - clientes (dict): Diccionario con clientes para resolver nombres.
        - accesorios (dict): Diccionario con accesorios para resolver nombres.
    Salida: Ninguna (solo visualización en pantalla con ID, fecha, cliente, producto, cantidad y total).
    """
    print(">>> INFORME LIBRE: LISTADO DETALLADO DE ALQUILERES")
    for anio, datos_anio in alquileres.items():
        for id_alq, d in datos_anio.items():
            cliente = clientes.get(d.get("Cliente"), {}).get("Nombre", d.get("Cliente"))
            producto = accesorios.get(d.get("Producto"), {}).get("Nombre", d.get("Producto"))
            print(f"{id_alq} | {d.get('FechaHora')} | Cliente: {cliente} | Producto: {producto} | Cant: {d.get('Cantidad')} | Total: {d.get('Total')}")


def informe_stock_resumen(accesorios: dict):
    """
    Objetivo: Mostrar un resumen del estado actual del inventario (stock y pérdidas/roturas).
    Entrada: 
        - accesorios (dict): Diccionario con los accesorios existentes.
    Salida: Ninguna (solo visualización en pantalla con código, nombre, stock y cantidad de pérdidas/roturas).
    """
    print(">>> INFORME: RESUMEN DE PRODUCTOS (stock / perdidos/rotos)")
    encabezado = f"{'CÓDIGO':8} {'NOMBRE':30} {'STOCK':6} {'PERDIDOS/ROTOS':15}"
    print(encabezado)
    print("-" * len(encabezado))
    for codigo, p in accesorios.items():
        print(f"{codigo:8} {p.get('Nombre',''):30} {str(p.get('Stock')):6} {str(p.get('PerdidosRotura')):15}")


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables (3 diccionarios de diccionarios - entidades maestras)
    #-------------------------------------------------
    """
    clientes = {
        # clave: código string -> valor: dict atributos (incluye 'Telefonos' dict)
        "C001": {"Nombre": "Gonzalo Perez", "Edad": 28, "DNI": "30111222", "Email": "gonzalo@example.com", "Telefonos": {"3411234567": True}, "Activo": True},
        "C002": {"Nombre": "María López", "Edad": 34, "DNI": "30122333", "Email": "maria@example.com", "Telefonos": {"3412345678": True,"3419876543": True}, "Activo": True},
        "C003": {"Nombre": "Juan García", "Edad": 45, "DNI": "30133444", "Email": "", "Telefonos": {"3415550000": True}, "Activo": True},
        "C004": {"Nombre": "Lucía Fernández", "Edad": 22, "DNI": "30144555", "Email": "lucia@example.com", "Telefonos": {"3416661111": True}, "Activo": True},
        "C005": {"Nombre": "Carlos Sánchez", "Edad": 50, "DNI": "30155666", "Email": "", "Telefonos": {"3417772222": True}, "Activo": True},
        "C006": {"Nombre": "Verónica Ruiz", "Edad": 29, "DNI": "30166777", "Email": "vero@example.com", "Telefonos": {"3418883333": True,"3419994444": True}, "Activo": True},
        "C007": {"Nombre": "Diego Martín", "Edad": 31, "DNI": "30177888", "Email": "", "Telefonos": {"3411010101": True}, "Activo": True},
        "C008": {"Nombre": "Romina Díaz", "Edad": 27, "DNI": "30188999", "Email": "romi@example.com", "Telefonos": {"3411212121": True}, "Activo": True},
        "C009": {"Nombre": "Pedro Alvarez", "Edad": 38, "DNI": "30199000", "Email": "", "Telefonos": {"3411313131": True}, "Activo": True},
        "C010": {"Nombre": "Ana Molina", "Edad": 24, "DNI": "30200111", "Email": "ana@example.com", "Telefonos": {"3411414141": True}, "Activo": True}
    }

    accesorios = {
        # atributo multivalor: 'Talles'  de códigos de talles
        "P001": {"Nombre": "Esquí Adulto", "PrecioDiario": 5000, "Stock": 10, "PerdidosRotura": 0, "Talles": {"T01": True,"T02": True}, "Activo": True},
        "P002": {"Nombre": "Botas Adulto", "PrecioDiario": 3000, "Stock": 15, "PerdidosRotura": 1, "Talles": {"T02": True,"T03": True}, "Activo": True},
        "P003": {"Nombre": "Bastones", "PrecioDiario": 800, "Stock": 20, "PerdidosRotura": 0, "Talles": {}, "Activo": True},
        "P004": {"Nombre": "Casco", "PrecioDiario": 700, "Stock": 25, "PerdidosRotura": 0, "Talles": {"T01": True,"T03": True}, "Activo": True},
        "P005": {"Nombre": "Pantalón térmico", "PrecioDiario": 900, "Stock": 12, "PerdidosRotura": 0, "Talles": {"T02": True,"T03": True,"T04": True}, "Activo": True},
        "P006": {"Nombre": "Campera térmica", "PrecioDiario": 1500, "Stock": 8, "PerdidosRotura": 0, "Talles": {"T03": True}, "Activo": True},
        "P007": {"Nombre": "Guantes", "PrecioDiario": 300, "Stock": 30, "PerdidosRotura": 2, "Talles": {"T01": True,"T02": True}, "Activo": True},
        "P008": {"Nombre": "Gafas", "PrecioDiario": 250, "Stock": 40, "PerdidosRotura": 0, "Talles": {}, "Activo": True},
        "P009": {"Nombre": "Protector espalda", "PrecioDiario": 1200, "Stock": 5, "PerdidosRotura": 0, "Talles": {"T02": True}, "Activo": True},
        "P010": {"Nombre": "Mochila porta esquí", "PrecioDiario": 1100, "Stock": 7, "PerdidosRotura": 0, "Talles": {}, "Activo": True}
    }

    talles = {
        # atributo multivalor: 'Equivalencias' 
        "T01": {"Nombre": "S", "Equivalencias": {"36": True,"38": True}, "Activo": True},
        "T02": {"Nombre": "M", "Equivalencias": {"40": True,"42": True}, "Activo": True},
        "T03": {"Nombre": "L", "Equivalencias": {"44": True,"46": True}, "Activo": True},
        "T04": {"Nombre": "XL", "Equivalencias": {"48": True,"50": True}, "Activo": True},
        "T05": {"Nombre": "Niño XS", "Equivalencias": {"28": True,"30": True}, "Activo": True},
        "T06": {"Nombre": "Niño S", "Equivalencias": {"32": True,"34": True}, "Activo": True},
        "T07": {"Nombre": "Unisex único", "Equivalencias": {}, "Activo": True},
        "T08": {"Nombre": "Extra L", "Equivalencias": {"52": True}, "Activo": True},
        "T09": {"Nombre": "Junior", "Equivalencias": {"30": True,"32": True}, "Activo": True},
        "T10": {"Nombre": "Bebe", "Equivalencias": {"24": True}, "Activo": True}
    }

    alquileres = {
        # Ejemplo inicial con 10 operaciones (año 2025) siguiendo la estructura usada en registrar_alquiler()
        "2025": {
            "ALQ0001": {
                "FechaHora": "2025.10.01 09:12:00",
                "Cliente": "C001",
                "Producto": "P001",
                "Cantidad": 1,
                "PrecioUnit": 5000,
                "Total": 5000
            },
            "ALQ0002": {
                "FechaHora": "2025.10.02 10:30:00",
                "Cliente": "C002",
                "Producto": "P002",
                "Cantidad": 2,
                "PrecioUnit": 3000,
                "Total": 6000
            },
            "ALQ0003": {
                "FechaHora": "2025.10.03 11:00:00",
                "Cliente": "C003",
                "Producto": "P003",
                "Cantidad": 3,
                "PrecioUnit": 800,
                "Total": 2400
            },
            "ALQ0004": {
                "FechaHora": "2025.10.04 12:15:00",
                "Cliente": "C004",
                "Producto": "P004",
                "Cantidad": 1,
                "PrecioUnit": 700,
                "Total": 700
            },
            "ALQ0005": {
                "FechaHora": "2025.10.05 13:45:00",
                "Cliente": "C005",
                "Producto": "P005",
                "Cantidad": 2,
                "PrecioUnit": 900,
                "Total": 1800
            },
            "ALQ0006": {
                "FechaHora": "2025.10.06 14:20:00",
                "Cliente": "C006",
                "Producto": "P006",
                "Cantidad": 1,
                "PrecioUnit": 1500,
                "Total": 1500
            },
            "ALQ0007": {
                "FechaHora": "2025.10.07 15:05:00",
                "Cliente": "C007",
                "Producto": "P007",
                "Cantidad": 4,
                "PrecioUnit": 300,
                "Total": 1200
            },
            "ALQ0008": {
                "FechaHora": "2025.10.08 16:40:00",
                "Cliente": "C008",
                "Producto": "P008",
                "Cantidad": 2,
                "PrecioUnit": 250,
                "Total": 500
            },
            "ALQ0009": {
                "FechaHora": "2025.10.09 17:10:00",
                "Cliente": "C009",
                "Producto": "P009",
                "Cantidad": 1,
                "PrecioUnit": 1200,
                "Total": 1200
            },
            "ALQ0010": {
                "FechaHora": "2025.10.10 18:00:00",
                "Cliente": "C010",
                "Producto": "P010",
                "Cantidad": 3,
                "PrecioUnit": 1100,
                "Total": 3300
            }
        },
        "2024": {
            "ALQ1011": {
                "FechaHora": "2024.08.01 09:10:00",
                "Cliente": "C010",
                "Producto": "P001",
                "Cantidad": 1,
            "PrecioUnit": 5000, 
            "Total": 5000
            },
            "ALQ1012": {
                "FechaHora": "2024.08.03 10:25:00",
                "Cliente": "C009",
                "Producto": "P004",
                "Cantidad": 2, 
                "PrecioUnit": 700, 
                "Total": 1400
                },
            "ALQ1013": {
                "FechaHora": "2024.08.05 11:40:00",
                "Cliente": "C008",
                "Producto": "P008",
                "Cantidad": 3, 
                "PrecioUnit": 250, 
                "Total": 750
                },
            "ALQ1014": {
                "FechaHora": "2024.08.07 12:55:00",
                "Cliente": "C007",
                "Producto": "P006",
                "Cantidad": 1, 
                "PrecioUnit": 1500, 
                "Total": 1500
                },
            "ALQ1015": {
                "FechaHora": "2024.08.09 14:10:00",
                "Cliente": "C006",
                "Producto": "P010",
                "Cantidad": 2, 
                "PrecioUnit": 1100, 
                "Total": 2200
                },
            "ALQ1016": {
                "FechaHora": "2024.08.11 15:30:00",
                "Cliente": "C005",
                "Producto": "P002",
                "Cantidad": 2, 
                "PrecioUnit": 3000, 
                "Total": 6000
                },
            "ALQ1017": {
                "FechaHora": "2024.08.13 16:45:00",
                "Cliente": "C004",
                "Producto": "P005",
                "Cantidad": 1, 
                "PrecioUnit": 900, 
                "Total": 900
                },
            "ALQ1018": {
                "FechaHora": "2024.08.15 17:55:00",
                "Cliente": "C003",
                "Producto": "P007",
                "Cantidad": 2, 
                "PrecioUnit": 300, 
                "Total": 600
                },
            "ALQ1019": {
                "FechaHora": "2024.08.17 18:25:00",
                "Cliente": "C002",
                "Producto": "P009",
                "Cantidad": 1, 
                "PrecioUnit": 1200, 
                "Total": 1200
                },
            "ALQ1020": {
                "FechaHora": "2024.08.19 19:05:00",
                "Cliente": "C001",
                "Producto": "P003",
                "Cantidad": 4, 
                "PrecioUnit": 800, 
                "Total": 3200
                }
    }
    }
    """

    #-------------------------------------------------
    # Bloque de menú 
    #-------------------------------------------------
    running = True
    while running:
        opciones = 5
        opcionMenuPrincipal = None
        valido = False
        while not valido:
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de clientes")
            print("[2] Gestión de accesorios")
            print("[3] Gestión de talles")
            print("[4] Gestión de alquileres / Informes")
            print("[0] Salir del programa")
            print("---------------------------")
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones)]:
                valido = True
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0":
            print("Saliendo...")
            running = False

        elif opcionMenuPrincipal == "1":
            # Submenú Clientes 
            clientes_running = True
            while clientes_running:
                opciones_sub = 4
                opcionSub = None
                valido_sub = False
                while not valido_sub:
                    print()
                    print("---------------------------")
                    print("MENÚ > GESTIÓN DE CLIENTES")
                    print("---------------------------")
                    print("[1] Ingresar cliente")
                    print("[2] Modificar cliente")
                    print("[3] Eliminar cliente (baja lógica)")
                    print("[4] Listado de clientes Activos")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    opcionSub = input("Seleccione una opción: ")
                    if opcionSub in [str(i) for i in range(0, opciones_sub + 1)]:
                        valido_sub = True
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSub == "0":
                    clientes_running = False
                else:
                    if opcionSub == "1":
                        clientes = alta_cliente(clientes)
                    elif opcionSub == "2":
                        clientes = modificar_cliente(clientes)
                    elif opcionSub == "3":
                        clientes = baja_logica_cliente(clientes)
                    elif opcionSub == "4":
                        listar_clientes_activos(clientes)

                    pausar()
                    print("\n\n")

        elif opcionMenuPrincipal == "2":
            # Submenú Accesorios 
            accesorios_running = True
            while accesorios_running:
                opciones_sub = 6
                opcionSub = None
                valido_sub = False
                while not valido_sub:
                    print()
                    print("---------------------------")
                    print("MENÚ > GESTIÓN DE ACCESORIOS")
                    print("---------------------------")
                    print("[1] Ingresar producto")
                    print("[2] Modificar producto")
                    print("[3] Eliminar producto (baja lógica)")
                    print("[4] Listado de productos en stock")
                    print("[5] Listado de ítems perdidos/rotos")
                    print("[6] Listado de talles por producto")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    opcionSub = input("Seleccione una opción: ")
                    if opcionSub in [str(i) for i in range(0, opciones_sub + 1)]:
                        valido_sub = True
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSub == "0":
                    accesorios_running = False
                else:
                    if opcionSub == "1":
                        accesorios = alta_accesorio(accesorios)
                    elif opcionSub == "2":
                        accesorios = modificar_accesorio(accesorios)
                    elif opcionSub == "3":
                        accesorios = baja_logica_accesorio(accesorios)
                    elif opcionSub == "4":
                        listar_productos_en_stock(accesorios)
                    elif opcionSub == "5":
                        listar_perdidos_rotos(accesorios)
                    elif opcionSub == "6":
                        listar_talles_producto(accesorios)

                    pausar()
                    print("\n\n")

        elif opcionMenuPrincipal == "3":
            # Submenú Talles 
            talles_running = True
            while talles_running:
                opciones_sub = 4
                opcionSub = None
                valido_sub = False
                while not valido_sub:
                    print()
                    print("---------------------------")
                    print("MENÚ > GESTIÓN DE TALLES")
                    print("---------------------------")
                    print("[1] Ingresar talle")
                    print("[2] Modificar talle")
                    print("[3] Eliminar talle (baja lógica)")
                    print("[4] Listado de talles Activos")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    opcionSub = input("Seleccione una opción: ")
                    if opcionSub in [str(i) for i in range(0, opciones_sub + 1)]:
                        valido_sub = True
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSub == "0":
                    talles_running = False
                else:
                    if opcionSub == "1":
                        talles = alta_talle(talles)
                    elif opcionSub == "2":
                        talles = modificar_talle(talles,accesorios)
                    elif opcionSub == "3":
                        talles = baja_logica_talle(talles)
                    elif opcionSub == "4":
                        listar_talles_activos(talles)

                    pausar()
                    print("\n\n")

        elif opcionMenuPrincipal == "4":
            # Submenú Alquileres / Informes (controlado por flag)
            alquileres_running = True
            while alquileres_running:
                opciones_sub = 4
                opcionSub = None
                valido_sub = False
                while not valido_sub:
                    print()
                    print("---------------------------")
                    print("MENÚ > ALQUILERES / INFORMES")
                    print("---------------------------")
                    print("[1] Registro de alquileres")
                    print("[2] Informes - Alquileres del Mes")
                    print("[3] Informes - Resumen Anual")
                    print("[4] Informe libre / Resumen stock")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    opcionSub = input("Seleccione una opción: ")
                    if opcionSub in [str(i) for i in range(0, opciones_sub + 1)]:
                        valido_sub = True
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSub == "0":
                    alquileres_running = False
                else:
                    if opcionSub == "1":
                        alquileres = registrar_alquiler(alquileres, clientes, accesorios)
                    elif opcionSub == "2":
                        listar_alquileres_mes_actual(alquileres, clientes, accesorios)
                    elif opcionSub == "3":
                        informe_resumen_anual(alquileres, clientes, accesorios)
                    elif opcionSub == "4":
                        informe_libre_eleccion(alquileres, clientes, accesorios)
                        informe_stock_resumen(accesorios)

                    pausar()
                    print("\n\n")


if __name__ == "__main__":
    main()
