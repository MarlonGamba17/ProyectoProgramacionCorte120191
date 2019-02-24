
TASA_IVA = 0.19
TARIFA_HORA = 100000
TASA_EXTRA = 0.25
TARIFA_RECARGO_ENVIO = 115

def calcular_precio_producto(coste_producto):
    precio_producto_sin_iva = coste_producto * 1.5
    precio_producto = precio_producto_sin_iva + calcular_iva_producto(precio_producto_sin_iva, TASA_IVA)

    return precio_producto


def calcular_precio_servicio(cantidad_horas):
    pass


def calcular_precio_servicio_extras(cantidad_horas):
    precio_servicio_sin_recargo_extras = cantidad_horas * TARIFA_HORA
    precio_servicio_extras = precio_servicio_sin_recargo_extras + (precio_servicio_sin_recargo_extras * TASA_EXTRA)

    return precio_servicio_extras


def calcular_costo_envio(kilometros):
    pass

def calcular_precio_producto_fuera(coste_producto, kilometros):
    precio_producto_con_envio = coste_producto + calcular_costo_envio(kilometros)
    precio_producto_fuera = precio_producto_con_envio + calcular_iva_producto(precio_producto_con_envio, TASA_IVA)
    return precio_producto_fuera


def calcular_iva_producto(coste_producto, tasa):
    pass


def calcular_iva_servicio(cantidad_horas, tasa):
    pass


def calcular_iva_envio(kilometros, tasa):
    pass


def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    pass


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    pass

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    pass


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    pass