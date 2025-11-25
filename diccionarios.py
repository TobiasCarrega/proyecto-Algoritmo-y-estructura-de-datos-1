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