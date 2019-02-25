
COMISION_VENTA = 0.5
TARIFA_HORA = 100000
TASA_EXTRA = 0.25
TARIFA_RECARGO_ENVIO = 115

def calcular_precio_producto(coste_producto):
    precio_producto = coste_producto + (coste_producto * COMISION_VENTA)

    return precio_producto


def calcular_precio_servicio(cantidad_horas):
    precio_servicio = cantidad_horas * TARIFA_HORA
    
    return precio_servicio


def calcular_precio_servicio_extras(cantidad_horas):
    precio_servicio_sin_recargo_extras = calcular_precio_servicio(cantidad_horas)
    precio_servicio_extras = precio_servicio_sin_recargo_extras + (precio_servicio_sin_recargo_extras * TASA_EXTRA)

    return precio_servicio_extras


def calcular_costo_envio(kilometros):
    costo_envio = TARIFA_RECARGO_ENVIO * kilometros

    return costo_envio


def calcular_precio_producto_fuera(coste_producto, kilometros):
    precio_producto_fuera = coste_producto + calcular_costo_envio(kilometros)

    return precio_producto_fuera


def calcular_iva_producto(coste_producto, tasa):
    pass


def calcular_iva_servicio(cantidad_horas, tasa):
    precio_servicio = calcular_precio_servicio(cantidad_horas)
    iva_servicio = precio_servicio * tasa

    return iva_servicio


def calcular_iva_envio(kilometros, tasa):
    pass


def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    pass


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    recaudo_locales = calcular_precio_producto(coste_producto_1) + \
                      calcular_precio_producto(coste_producto_2) + \
                      calcular_precio_producto(coste_producto_3)

    return recaudo_locales

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    pass


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    recaudo_mixto_local = calcular_precio_producto(coste_producto_1) + \
                          calcular_precio_producto(coste_producto_2) + \
                          calcular_precio_servicio(horas_1) + \
                          calcular_precio_servicio(horas_2)

    return recaudo_mixto_local