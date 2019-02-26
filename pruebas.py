import unittest
import funciones as f

class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):
        self.assertEqual(f.calcular_precio_producto(1000),1500.0)
        self.assertEqual(f.calcular_precio_producto(0),0)
        self.assertEqual(f.calcular_precio_producto(2500),3750.0)

    def test_calcular_precio_servicio(self):
        self.assertEqual(f.calcular_precio_servicio(48),4800000.0)
        self.assertEqual(f.calcular_precio_servicio(0),0.0)
        self.assertEqual(f.calcular_precio_servicio(100000000),10000000000000.0)

    def test_calcular_precio_servicio_extras(self):
        self.assertEqual(f.calcular_precio_servicio_extras(6), 750000.0)
        self.assertEqual(f.calcular_precio_servicio_extras(10), 1250000.0)

    def test_calcular_costo_envio(self):
        self.assertEqual(f.calcular_costo_envio(289),33235.0)
        self.assertEqual(f.calcular_costo_envio(0),0.0)

    def test_calcular_precio_producto_fuera(self):
        self.assertEqual(f.calcular_precio_producto_fuera(1000, 4), 1960.0)
        self.assertEqual(f.calcular_precio_producto_fuera(2000, 6), 3690.0)

    def test_calcular_iva_producto(self):
        self.assertEqual(f.calcular_iva_producto(100000,0.19),28500.0)
        self.assertEqual(f.calcular_iva_producto(0,0),0.0)

    def test_calcular_iva_servicio(self):
        self.assertEqual(f.calcular_iva_servicio(3, 0.19), 57000.0)
        self.assertEqual(f.calcular_iva_servicio(2, 0.16), 32000.0)

    def test_calcular_iva_envio(self):
        self.assertEqual(f.calcular_iva_envio(20, 0.19), 437.0)
        self.assertEqual(f.calcular_iva_envio(30, 0.12), 414.0)

    def test_calcular_iva_servicio_extra(self):
        self.assertEqual(f.calcular_iva_servicio_extra(15, 0.8),1500000.0)
        self.assertEqual(f.calcular_iva_servicio_extra(0, 0.8),0)

    def test_calcular_recaudo_locales(self):
        self.assertEqual(f.calcular_recaudo_locales(1000, 2000, 3000), 9000.0)
        self.assertEqual(f.calcular_recaudo_locales(2000, 1200,   0 ), 4800.0)
        self.assertEqual(f.calcular_recaudo_locales(800,  700 ,   1 ), 2251.5)     

    def test_calcular_recaudo_horas_extra(self):
        self.assertEqual(f.calcular_recaudo_horas_extra(2.5, 5, 6, 18), 3937500.0)
        self.assertEqual(f.calcular_recaudo_horas_extra(0, 0, 0, 0), 0)

    def test_calcular_recaudo_mixto_local(self):
        self.assertEqual(f.calcular_recaudo_mixto_local(34000, 59000, 34, 10),4539500.0)
        self.assertEqual(f.calcular_recaudo_mixto_local(4000, 23000, 14, 1), 1540500.0)

if __name__ == 'main':
    unittest.main()
