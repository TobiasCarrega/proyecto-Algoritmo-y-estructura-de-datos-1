#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# ---------------------------
# INFORMES MENSUALES
# ---------------------------

def listar_alquileres_mes_actual(alquileres: dict):
    """
    Muestra todos los alquileres correspondientes al mes y año actual.
    """
    print(">>> INFORME MENSUAL DE ALQUILERES (MES ACTUAL)")
    anio = time.strftime("%Y")
    mes_actual = time.strftime("%m")

    if anio not in alquileres:
        print("No hay alquileres cargados para este año.")
        return

    print(f"{'FECHA':20} {'CLIENTE':10} {'PRODUCTO':10} {'CANT':4} {'DIAS':4} {'TOTAL':8}")
    print("-" * 70)

    for clave, datos in alquileres[anio].items():
        fecha = datos["FechaHora"]
        mes_alquiler = fecha[5:7]

        if mes_alquiler == mes_actual:
            print(f"{fecha:20} {datos['Cliente']:10} {datos['Producto']:10} "
                  f"{str(datos['Cantidad']):4} {str(datos['Dias']):4} {str(datos['Total']):8}")


# ---------------------------
# INFORMES DE STOCK
# ---------------------------

def informe_stock_total(accesorios: dict):
    """
    Informa el stock disponible de cada accesorio.
    """
    print(">>> INFORME DE STOCK TOTAL")
    print(f"{'CÓDIGO':8} {'NOMBRE':30} {'STOCK':6} {'ROTOS/LOST':10}")
    print("-" * 60)

    for codigo, datos in accesorios.items():
        print(f"{codigo:8} {datos['Nombre'][:30]:30} "
              f"{str(datos['Stock']):6} {str(datos['PerdidosRotura']):10}")


# ==============================================================================================
# NUEVO: **INFORMES ANUALES (PEDIDOS POR EL PROFESOR)**
# ==============================================================================================

def informe_anual_por_cliente(alquileres: dict, clientes: dict, anio: str):
    """
    Informe ANUAL: cantidad de alquileres realizados por cada cliente.

    Parámetros:
        alquileres: dict con estructura {anio: {clave: datos}}
        clientes: dict con datos del cliente
        anio: año a consultar
    """
    print(f">>> INFORME ANUAL POR CLIENTE ({anio})")

    if anio not in alquileres:
        print("No hay alquileres cargados en ese año.")
        return

    contador = {}   # cliente -> cantidad de alquileres

    for clave, datos in alquileres[anio].items():
        cli = datos["Cliente"]
        contador[cli] = contador.get(cli, 0) + 1

    print(f"{'CLIENTE':10} {'NOMBRE':25} {'ALQUILERES':10}")
    print("-" * 50)

    for cli, cant in contador.items():
        nombre = clientes.get(cli, {}).get("Nombre", "Desconocido")
        print(f"{cli:10} {nombre[:25]:25} {cant:10}")


def informe_recaudacion_anual(alquileres: dict, anio: str):
    """
    Informe ANUAL: recaudación total del año.

    Parámetros:
        alquileres: dict general de alquileres
        anio: año a consultar
    """
    print(f">>> INFORME ANUAL DE RECAUDACIÓN ({anio})")

    if anio not in alquileres:
        print("No hay datos de ese año.")
        return

    total = 0

    for clave, datos in alquileres[anio].items():
        total += datos.get("Total", 0)

    print(f"Recaudación total del año {anio}: ${total}")
