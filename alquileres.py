#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time   # Se usa para generar fecha/hora y calcular diferencia de días


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# ---------------------------
# Utilidades
# ---------------------------

def fecha_hora_actual():
    """
    Devuelve la fecha y hora actual con formato requerido por la cátedra:
    "AAAA.MM.DD hh:mm:ss"
    """
    return time.strftime("%Y.%m.%d %H:%M:%S")


# ---------------------------
# Gestión de Alquileres
# ---------------------------

def registrar_alquiler(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Registra una operación de alquiler.
    Pasos:
        - Verifica cliente activo
        - Verifica accesorio activo y con stock
        - Solicita cantidad
        - Genera clave del alquiler usando fecha y hora
        - Pide fecha de devolución
        - Calcula días (mínimo 1)
        - Calcula monto total según días
        - Descarga stock del accesorio
        - Guarda la operación en el diccionario 'alquileres'
    """
    print(">>> REGISTRAR ALQUILER")
    
    anio = time.strftime("%Y")
    if anio not in alquileres:
        alquileres[anio] = {}

    # Validar cliente
    codigo_cliente = input("Código cliente: ").strip().upper()
    if codigo_cliente not in clientes or not clientes[codigo_cliente].get("Activo", False):
        print("Cliente inválido o inactivo.")
        return alquileres

    # Validar producto
    codigo_producto = input("Código producto: ").strip().upper()
    if codigo_producto not in accesorios or not accesorios[codigo_producto].get("Activo", False):
        print("Producto inválido o inactivo.")
        return alquileres

    # Validar cantidad
    cantidad_raw = input("Cantidad a alquilar: ").strip()
    if not cantidad_raw.isdigit() or int(cantidad_raw) <= 0:
        print("Cantidad inválida.")
        return alquileres
    cantidad = int(cantidad_raw)

    # Verificar stock
    if accesorios[codigo_producto].get("Stock", 0) < cantidad:
        print("Stock insuficiente.")
        return alquileres

    precio_unit = accesorios[codigo_producto].get("PrecioDiario", 0)

    # FECHA INICIO = clave del alquiler
    fh = fecha_hora_actual()

    clave_alquiler = fh  # clave basada en fecha
    # Evita que se repitan claves si se alquilan varios en el mismo segundo
    if clave_alquiler in alquileres[anio]:
        clave_alquiler = fh + f"-{len(alquileres[anio]) + 1}"

    # Solicitar fecha de devolución
    print("\nIngrese fecha de devolución (AAAA.MM.DD hh:mm:ss)")
    fecha_fin = input("Fecha fin: ").strip()

    try:
        time.strptime(fecha_fin, "%Y.%m.%d %H:%M:%S")
    except:
        print("Fecha inválida. Se aplicará 1 día de alquiler.")
        fecha_fin = fh

    # Calcular días de diferencia
    inicio = time.strptime(fh, "%Y.%m.%d %H:%M:%S")
    fin = time.strptime(fecha_fin, "%Y.%m.%d %H:%M:%S")
    t_inicio = time.mktime(inicio)
    t_fin = time.mktime(fin)

    if t_fin <= t_inicio:
        dias = 1
    else:
        dias = int((t_fin - t_inicio) // 86400)
        dias = max(1, dias)

    # Calcular total
    total = precio_unit * cantidad * dias

    # Guardar alquiler
    alquileres[anio][clave_alquiler] = {
        "FechaHora": fh,
        "FechaFin": fecha_fin,
        "Dias": dias,
        "Cliente": codigo_cliente,
        "Producto": codigo_producto,
        "Cantidad": cantidad,
        "PrecioUnit": precio_unit,
        "Total": total
    }

    # Actualizar stock
    accesorios[codigo_producto]["Stock"] -= cantidad

    print(f"Alquiler registrado correctamente:")
    print(f"Clave: {clave_alquiler}")
    print(f"Cliente: {codigo_cliente} | Producto: {codigo_producto}")
    print(f"Cantidad: {cantidad} | Días: {dias} | Total: ${total}")

    return alquileres
