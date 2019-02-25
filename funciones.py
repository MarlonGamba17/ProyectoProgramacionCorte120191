
COMISION_VENTA = 0.5
TARIFA_HORA = 100000
TASA_EXTRA = 0.25
TARIFA_RECARGO_ENVIO = 115

def calcular_precio_producto(coste_producto):
    '''
    (float) -> float

    Calcular el precio del producto dado el costo del producto

    coste_producto = float contiene el valor neto del producto
    precio_producto = float contiene el precio del procducto sin iva mas el Iva
    COMISION_VENTA = float contiene la comision de venta

    return = float retorna el precio del producto incluyendo la comision de venta
    '''
    precio_producto = coste_producto + (coste_producto * COMISION_VENTA)

    return precio_producto


def calcular_precio_servicio(cantidad_horas):
    '''
    (float) -> float

    Calcular el precio del servicio dada la cantidad de horas laboradas

    precio_servicio = float contiene el precio del servicio sin iva
    cantidad_hora = float contiene el numero de horas de servicio
    TARIFA_HORA = float contiene la tarifa por hora

    return = float retorna el precio del servicio multiplicado por el valor de la tarifa por hora
    '''
    precio_servicio = cantidad_horas * TARIFA_HORA
    
    return precio_servicio


def calcular_precio_servicio_extras(cantidad_horas):
    '''
    (float) -> float
    
    Calcular el precio de  las horas extras prestadas en un servicio dada la cantidad de horas extras

    TASA EXTRA = float contiene el valor de la tasa extra asignado al 25%
    cantdad_horas = float contiene la cantidad de horas extras prestadas en el servicio
    precio_servicio_sin_recargo_extras = float contiene el precio de servicio sin el recargo de horas extras
    precio_servicio_extras = float contiene el precio de servicio con el recago de las horas extras
    
    return = float retorna al valor de servicio con extras
    '''
    precio_servicio_sin_recargo_extras = calcular_precio_servicio(cantidad_horas)
    precio_servicio_extras = precio_servicio_sin_recargo_extras + (precio_servicio_sin_recargo_extras * TASA_EXTRA)

    return precio_servicio_extras


def calcular_costo_envio(kilometros):
    '''
    (float) -> float

    Calcular el costo del envio dada la cantidad de kilometros

    costo_envio = float contiene el valor del envio dada la cantidad de kilometros recorridos
    TARIFA_RECARGO_ENVIO = float contiene la tarifa de recargo dada 115
    kilometros = float contiene los kilometros recorridos

    return = float retorna la tarifa de recargo de envio multiplicada por los kilometros
    '''
    costo_envio = TARIFA_RECARGO_ENVIO * kilometros

    return costo_envio


def calcular_precio_producto_fuera(coste_producto, kilometros):
    '''
    (float,float) -> float

    Calcular el precio del producto cuando se vende fuera de la ciudad

    precio_producto_fuera = float contiene el costo del producto mas el costo del envio
    coste_producto = float contiene el valor neto del producto
    kilometros =float representa el numero de kilometros desde el punto de envio
    
    return float retorna el precio del producto incluyendo el costo de envio 
    '''
    precio_producto_fuera = calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)

    return precio_producto_fuera


def calcular_iva_producto(coste_producto, tasa):
    '''
    (float,float) ->float

    calcular el iva del producto

    calcular_precio_producto(coste_producto) = float contiene el precio del producto incluyendo la comision de venta
    tasa = float representa la tasa del iva aplicada al servicio
    iva_producto = float contiene el iva definido segun la tasa dada

    return float retorna el calculo del iva para un producto
    '''
    iva_producto= calcular_precio_producto(coste_producto) * tasa

    return iva_producto
    

def calcular_iva_servicio(cantidad_horas, tasa):
    '''
    (float,float) ->float
    
    calcular el iva del servicio
    
    tasa float representa la tasa del iva aplicada al servicio
    precio_servicio= float contiene el precio total del servicio
    cantidad_horas= float contiene la cantidad de horas prestadas en el servicio
    iva_servicio= float contiene el iva calculado segun la tasa dada

    return float retorna el valor del iva para un servicio
    '''
    precio_servicio = calcular_precio_servicio(cantidad_horas)
    iva_servicio = precio_servicio * tasa

    return iva_servicio


def calcular_iva_envio(kilometros, tasa):
    '''
    (float, float) -> float

    Calcula el iva del envio

    kilometros = float contiene el nùmero de kilometros desde el punto de envio
    tasa = float contiene la tasa del iva fijada para el costo del envio
    iva_envio = float contiene el iva calculado para el envio segun la tasa dada

    return float retorna el valor del iva para el costo de envio
    '''
    iva_envio = calcular_costo_envio(kilometros) * tasa

    return iva_envio


def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    '''
    (float,float) ->float

    calcular el iva del servicio fuera

    precio_servicio = float contiene el precio total del servicio
    calcular_precio_producto_fuera = float contiene el precio del producto incluyendo el costo de envio
    cantidad_horas = float contiene la cantidad de horas prestadas en el servicio
    iva_servicio = float contiene el iva definido segun la tasa dada
    tasa = float representa la tasa del iva aplicada al servicio

    return float retorna el calculo del iva para un servicio fuera
    '''
    precio_servicio = calcular_precio_servicio_fuera(cantidad_horas)
    iva_servicio = precio_servicio * tasa

    return iva_servicio


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    '''
    (float, float, float) -> float

    Calcular el recaudo total de la venta de 3 productos locales

    coste_producto_1 = float contiene el costo del primer producto
    coste_producto_2 = float contiene el costo del segundo producto
    coste_producto_3 = float contiene el costo del tercer producto
    recaudo_locales = float contene el valor total de la suma de los costos de los 3 productos vendidos

    return float retornar el recaudo de la venta de 3 productos locales
    '''
    recaudo_locales = calcular_precio_producto(coste_producto_1) + \
                      calcular_precio_producto(coste_producto_2) + \
                      calcular_precio_producto(coste_producto_3)

    return recaudo_locales


def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    '''
    (float, float, float, float) -> float

    Calcular el recaudo total de las horas extra

    horas_1 = float contiene la primer cantidad de horas extra
    horas_2 = float contiene la segunda cantidad de horas extra
    horas_3 = float contiene la terera cantidad de horas extra
    horas_4 = float contiene la cuarta cantidad de horas extra
    recaudo_horas_extra = float contene el valor total de la suma de los precios de las horas extra

    return float retornar el valor total de la suma de los precios de las horas extra
    '''
    recaudo_horas_extra = calcular_precio_servicio_extras(horas_1) \
                          + calcular_precio_servicio_extras(horas_2) \
                          + calcular_precio_servicio_extras(horas_3) \
                          + calcular_precio_servicio_extras(horas_4)


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    '''
    (float, float, float, float) -> float

    Calcular recaudo total de la venta de 2 productos y 2 servicios

    coste_producto_1 = float contiene el costo del primer producto
    coste_producto_2 = float contiene el costo del segundo producto
    horas_1 = float contiene el nùmero de horas del primer servicio
    horas_2 = float contiene el nùmero de horas del segundo servicio
    recaudo_mixto_local = float contiene el valor total de la suma de la venta de 2 productos y 2 servicios

    return = float retornar el valor total de la suma de la venta de 2 productos y 2 servicios
    '''
    recaudo_mixto_local = calcular_precio_producto(coste_producto_1) + \
                          calcular_precio_producto(coste_producto_2) + \
                          calcular_precio_servicio(horas_1) + \
                          calcular_precio_servicio(horas_2)

    return recaudo_mixto_local