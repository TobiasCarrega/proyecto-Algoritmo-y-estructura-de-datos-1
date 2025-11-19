#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time   # Necesario para obtener mes y año actuales


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# ---------------------------
# Informes de Alquileres
# ---------------------------

def listar_alquileres_mes_actual(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Informe 1:
    Muestra todas las operaciones de alquiler realizadas en el mes actual.
    Filtra por:
        año actual -> clave del diccionario
        mes actual -> tomado de la FechaHora ("AAAA.MM.DD hh:mm:ss")
    """
    print(">>> LISTADO DE ALQUILERES - MES ACTUAL")

    anio = time.strftime("%Y")
    mes_actual = time.strftime("%m")

    encabezado = (
        f"{'Fecha/Hora':20} {'Cliente':20} {'Producto':25} "
        f"{'Cant':5} {'Unitario':10} {'Total':12}"
    )
    print(encabezado)
    print("-" * len(encabezado))

    # Si no existe el año
    if anio not in alquileres:
        print("No hay operaciones registradas en el año actual.")
        return

    # Recorre todas las operaciones del año
    for clave, datos in alquileres[anio].items():
        fecha = datos.get("FechaHora", "")

        # Extrae mes (posiciones 5:7 en formato AAAA.MM.DD)
        if fecha[5:7] == mes_actual:
            cliente = clientes.get(datos.get("Cliente"), {}).get("Nombre", "N/D")
            producto = accesorios.get(datos.get("Producto"), {}).get("Nombre", "N/D")

            print(f"{fecha:20} "
                  f"{cliente[:20]:20} "
                  f"{producto[:25]:25} "
                  f"{str(datos.get('Cantidad')):5} "
                  f"{str(datos.get('PrecioUnit')):10} "
                  f"{str(datos.get('Total')):12}")


def informe_resumen_anual(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Informe 2 (corregido):
    Recorre TODOS los años disponibles y genera:
        - cantidad de alquileres en el año
        - unidades alquiladas
        - recaudación total
        - detalle de cada alquiler

    Este informe fue corregido porque el profesor pidió
    un verdadero "informe anual" y no solo un listado.
    """
    print(">>> RESUMEN ANUAL DE ALQUILERES")

    encabezado = (
        f"{'Año':5} {'Clave':20} {'Fecha/Hora':20} {'Cliente':20} "
        f"{'Producto':25} {'Cant':5} {'Unit':10} {'Total':10}"
    )
    print(encabezado)
    print("-" * len(encabezado))

    # Recorre TODOS los años cargados en el sistema
    for anio, datos_anuales in alquileres.items():
        total_operaciones = 0
        total_unidades = 0
        total_recaudado = 0

        for clave, datos in datos_anuales.items():
            fecha = datos.get("FechaHora", "")
            cliente = clientes.get(datos.get("Cliente"), {}).get("Nombre", "N/D")
            producto = accesorios.get(datos.get("Producto"), {}).get("Nombre", "N/D")
            cantidad = datos.get("Cantidad", 0)
            unitario = datos.get("PrecioUnit", 0)
            total = datos.get("Total", 0)

            # Acumular
            total_operaciones += 1
            total_unidades += cantidad
            total_recaudado += total

            # Mostrar detalle
            print(f"{anio:5} "
                  f"{clave:20} "
                  f"{fecha:20} "
                  f"{cliente[:20]:20} "
                  f"{producto[:25]:25} "
                  f"{str(cantidad):5} "
                  f"{str(unitario):10} "
                  f"{str(total):10}")

        # Resumen final del año
        print("-" * len(encabezado))
        print(f"Total de operaciones en {anio}: {total_operaciones}")
        print(f"Unidades alquiladas en {anio}: {total_unidades}")
        print(f"Recaudación total en {anio}: ${total_recaudado}")
        print("=" * len(encabezado))


def informe_libre_eleccion(alquileres: dict, clientes: dict, accesorios: dict):
    """
    Informe 3:
    Listado libre elegido por el equipo.
    En este caso, muestra claves, fechas, nombres de cliente y producto.
    """
    print(">>> INFORME LIBRE: DETALLE DE OPERACIONES")

    for anio, datos_anuales in alquileres.items():
        print(f"\n--- Año {anio} ---")

        for clave, datos in datos_anuales.items():
            cliente = clientes.get(datos.get("Cliente"), {}).get("Nombre", "N/D")
            producto = accesorios.get(datos.get("Producto"), {}).get("Nombre", "N/D")

            print(f"{clave} | "
                  f"{datos.get('FechaHora')} | "
                  f"{cliente} | "
                  f"{producto} | "
                  f"Cantidad: {datos.get('Cantidad')} | "
                  f"Total: ${datos.get('Total')}")


def informe_stock_resumen(accesorios: dict):
    """
    Informe 4:
    Muestra el estado general de stock y pérdidas/roturas de cada accesorio.
    """
    print(">>> INFORME: RESUMEN DE STOCK DE ACCESORIOS")

    encabezado = f"{'CÓDIGO':8} {'NOMBRE':30} {'STOCK':6} {'PERDIDOS/ROTOS':15}"
    print(encabezado)
    print("-" * len(encabezado))

    for codigo, p in accesorios.items():
        print(f"{codigo:8} "
              f"{p.get('Nombre','')[:30]:30} "
              f"{str(p.get('Stock')):6} "
              f"{str(p.get('PerdidosRotura')):15}")

    print("-" * len(encabezado))

