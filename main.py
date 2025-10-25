"""
-----------------------------------------------------------------------------------------------
Título: Entrega1 - Sistema de Alquiler de Accesorios para Esquí (versión inicial)
Fecha: 2025.10.15
Autor: Equipo 8  (plantilla inicial)
Descripción:
    Estructura inicial del programa: 3 entidades maestras (clientes, accesorios, talles),
    una entidad de transacciones (alquileres) y menú multinivel con funciones separadas.
Pendientes:
    - Completar validaciones particulares y lógica de stock/descuentos
    - Implementar informes detallados (resúmenes mensuales/anuales)
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time  # permitido en el enunciado para obtener fecha/hora
from clientes import cargar_clientes
from accesorios import cargar_accesorios
from productos import cargar_productos
from talles import cargar_talles
from alquileres import cargar_alquileres
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
# def alta_cliente(clientes):
#     codigo = f"C{len(clientes) + 1:03d}"
#     nombre = input("Nombre y Apellido: ")
#     edad = int(input("Edad: "))
#     dni = input("DNI: ")
#     email = input("Email: ")
#     telefono = input("Teléfono: ")
#     clientes[codigo] = {
#         "Nombre": nombre,
#         "Edad": edad,
#         "DNI": dni,
#         "Email": email,
#         "Telefonos": {telefono: True},
#         "Activo": True
#     }
#     print(f"Cliente {codigo} agregado correctamente.")
#     return clientes
# ---------------------------
# Utilidades
# ---------------------------
def fecha_hora_actual():
    """
    Devuelve la fecha/hora actual como string con formato "AAAA.MM.DD hh:mm:ss".
    """
    return time.strftime("%Y.%m.%d %H:%M:%S")


def validar_entero_en_rango(texto_input: str, min_val: int, max_val: int):
    """
    Pide por teclado un entero entre min_val y max_val (inclusive).
    Valida que la entrada sea numérica y esté en rango. Devuelve el entero aceptado.
    """
    while True:
        valor = input(texto_input).strip()
        if valor.isdigit():
            n = int(valor)
            if min_val <= n <= max_val:
                return n
        print(f"Error: ingrese un número entero entre {min_val} y {max_val}.")


def pausar():
    """Pausa estándar usada entre opciones."""
    input("\nPresione ENTER para volver al menú.")


# ---------------------------
# CRUD CLIENTES
# ---------------------------
def alta_cliente(clientes: dict):
    """
    Alta lógico de cliente. Código asignado automáticamente (C###).
    Telefonos se almacenan como dict {telefono: True, ...}
    Se obtiene el número del último cliente por slicing sobre la última clave.
    """
    print(">>> ALTA CLIENTE")

    # determinar próximo código a partir del último elemento del dict (preserva orden en Python 3.7+)
    if len(clientes) == 0:
        next_n = 1
    else:
        ultima_clave = list(clientes.keys())[-1]      # p.ej. "C010"
        numero_str = ultima_clave[1:]                 # slicing para capturar la parte numérica
        if numero_str.isdigit():
            next_n = int(numero_str) + 1
        else:
            # si el sufijo no es numérico, comenzar en 1
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
    Modifica datos de un cliente existente (si está activo o inactivo).
    Telefonos se almacenan como dict {telefono: True}
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
    Marca el cliente como inactivo (baja lógica).
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
    Muestra por pantalla los clientes con 'Activo' == True.
    Telefonos ahora se obtienen de las claves del dict.
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
def alta_accesorio(accesorios: dict) :
    """
    Alta de accesorio. Talles ahora como dict {talle_codigo: True, ...}
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
        "Talles": talles,   # multivalor como dict
        "Activo": True
    }
    print(f"Accesorio {codigo} cargado.")
    return accesorios


def modificar_accesorio(accesorios: dict) :
    """
    Modifica un accesorio existente. Talles como dict.
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


def baja_logica_accesorio(accesorios: dict) :
    """
    Marca un accesorio como inactivo (baja lógica).
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
    Muestra productos activos con stock > 0.
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
    Lista ítems perdidos/rotos (campo PerdidosRotura > 0).
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
    Muestra talles disponibles por producto (ahora claves del dict).
    """
    print(">>> LISTADO DE TALLES POR PRODUCTO")
    for codigo, p in accesorios.items():
        if p.get("Activo", False):
            print(f"{codigo} - {p.get('Nombre')}: {', '.join(p.get('Talles', {}).keys())}")


# ---------------------------
# CRUD TALLES (Entidad maestra 3)
# ---------------------------
def alta_talle(talles: dict) :
    """
    Alta de talle. Equivalencias ahora dict {equiv: True}
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
        "Equivalencias": equivalencias,  # multivalor como dict
        "Activo": True
    }
    print(f"Talle {codigo} dado de alta.")
    return talles


def modificar_talle(talles: dict, accesorios: dict) : 
    """
    Modifica un talle. Equivalencias como dict.
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


def baja_logica_talle(talles: dict) :
    """
    Baja lógica de un talle.
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
    Lista talles activos.
    """
    print(">>> LISTADO DE TALLES ACTIVOS")
    for codigo, t in talles.items():
        if t.get("Activo", False):
            print(f"{codigo}: {t.get('Nombre')} - Equiv: {', '.join(t.get('Equivalencias', {}).keys())}")


# ---------------------------
# ENTIDAD TRANSACCIONES: ALQUILERES (2 diccionarios anidados)
# ---------------------------
def registrar_alquiler(alquileres: dict, clientes: dict, accesorios: dict) :
    print(">>> REGISTRAR ALQUILER")
    anio = time.strftime("%Y")
    # generar ID simple (se cuenta cantidad actual + 1)
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

    # validar stock
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

    # actualizar stock (resta) - acción realizada en la versión 1.0 (simple)
    accesorios[codigo_producto]["Stock"] -= cantidad

    print(f"Alquiler registrado: {next_id} - {fh} - Cliente {codigo_cliente} - Producto {codigo_producto} - Cant {cantidad}")
    return alquileres


def listar_alquileres_mes_actual(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Informe 1: Listado de operaciones del mes en curso (formato tabular).
    Se recorre el año actual en alquileres y filtra por mes actual.
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
        if fecha[5:7] == mes:  # formato "AAAA.MM.DD hh:mm:ss" -> posiciones 5:7 son mes
            cliente_nombre = clientes.get(datos.get("Cliente"), {}).get("Nombre", datos.get("Cliente"))
            producto_nombre = accesorios.get(datos.get("Producto"), {}).get("Nombre", datos.get("Producto"))
            print(f"{fecha:20} {cliente_nombre[:20]:20} {producto_nombre[:25]:25} {str(datos.get('Cantidad')):6} {str(datos.get('PrecioUnit')):10} {str(datos.get('Total')):12}")


def informe_resumen_anual(alquileres: dict, clientes: dict, accesorios: dict):
    print(">>> LISTADO DE ALQUILERES - ANUAL")
    encabezado = f"{'Año':4}{'ID_Alquiler':12}{'Fecha/Hora':20}{'Cliente':20}{'Producto':25}{'Cant.':6}{'Unit.':10}{'Total':12}"
    print(encabezado)
    print("-" * len(encabezado))

    # recorrer todos los años
    for año, datos_anuales in alquileres.items():
        contador = 0
        recaudacion = 0
        unidades = 0

        # recorrer los alquileres de ese año
        for id_alq, datos in datos_anuales.items():
            fecha = datos.get("FechaHora", "")
            cliente_nombre = clientes.get(datos.get("Cliente"), {}).get("Nombre", datos.get("Cliente"))
            producto_nombre = accesorios.get(datos.get("Producto"), {}).get("Nombre", datos.get("Producto"))
            cantidad = datos.get("Cantidad", 0)
            unitario = datos.get("PrecioUnit", 0)
            total = datos.get("Total", 0)

            # acumuladores
            contador += 1
            recaudacion += total
            unidades += cantidad

            # imprimir detalle
            print(f"{año:4} {id_alq:12} {fecha:20} {cliente_nombre[:20]:20} {producto_nombre[:25]:25} {cantidad:6} {unitario:10} {total:12}")

        # resumen anual
        print("-" * len(encabezado))
        print(f">>> Total de alquileres en {año}: {contador}")
        print(f">>> Unidades alquiladas en {año}: {unidades}")
        print(f">>> Recaudación total en {año}: ${recaudacion}")
        print("=" * len(encabezado))


def informe_libre_eleccion(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Informe 4: Listado a libre elección del equipo. Se puede listar las transacciones
    con el nombre del cliente y nombre del producto (ejemplo).
    """
    print(">>> INFORME LIBRE: LISTADO DETALLADO DE ALQUILERES")
    for anio, datos_anio in alquileres.items():
        for id_alq, d in datos_anio.items():
            cliente = clientes.get(d.get("Cliente"), {}).get("Nombre", d.get("Cliente"))
            producto = accesorios.get(d.get("Producto"), {}).get("Nombre", d.get("Producto"))
            print(f"{id_alq} | {d.get('FechaHora')} | Cliente: {cliente} | Producto: {producto} | Cant: {d.get('Cantidad')} | Total: {d.get('Total')}")


def informe_stock_resumen(accesorios: dict):
    """
    Informe 4.2: Resumen de productos: stock, alquilados (implícito), perdidos/rotos.
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
    #Cargar los datos desde los archivos .txt
    clientes = cargar_clientes("clientes.txt")
    accesorios = cargar_accesorios("accesorios.txt")
    productos = cargar_productos("productos.txt")
    talles = cargar_talles("talles.txt")
    alquileres = cargar_alquileres("alquileres.txt")

    print(">>> Sistema de alquiler de esquí iniciado correctamente.\n")
    print(f"Clientes cargados: {len(clientes)}")
    print(f"Accesorios cargados: {len(accesorios)}")
    print(f"Productos cargados: {len(productos)}")
    print(f"Talles cargados: {len(talles)}")
    print(f"Alquileres cargados: {len(alquileres)}\n")

    print("Datos cargados correctamente. (Próximo paso: menú de opciones)")

    #Guarda los datos actualizados al salir del sistema 
    guardar_clientes("clientes.txt", clientes)
    guardar_accesorios("accesorios.txt", accesorios)
    guardar_productos("productos.txt", productos)
    guardar_talles("talles.txt", talles)
    guardar_alquileres("alquileres.txt", alquileres)

    print("\nCambios guardados correctamente en los archivos.")

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
