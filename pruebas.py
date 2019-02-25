import unittest
import funciones as f

class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):
        self.assertEqual(1600, f.calcular_precio_producto(1000))
        self.assertEqual(0, f.calcular_precio_producto(0))

    def test_calcular_precio_servicio(self):
        pass

    def test_calcular_precio_servicio_extras(self):
        self.assertEqual(750000.0, f.calcular_precio_servicio_extras(6))
        self.assertEqual(1250000.0, f.calcular_precio_servicio_extras(10))

    def test_calcular_costo_envio(self):
        pass

    def test_calcular_precio_producto_fuera(self):
        self.assertEqual(1960, f.calcular_precio_producto_fuera(1000, 4))
        self.assertEqual(3690, f.calcular_precio_producto_fuera(2000, 6))

    def test_calcular_iva_producto(self):
        pass

    def test_calcular_iva_servicio(self):
        self.assertEqual(57000, f.calcular_iva_servicio(3, 0.19))
        self.assertEqual(32000, f.calcular_iva_servicio(2, 0.16))

    def test_calcular_iva_envio(self):
        self.assertEqual(f.calcular_iva_envio(20, 0.19), 437)
        self.assertEqual(f.calcular_iva_envio(30, 0.12), 414)

    def test_calcular_iva_servicio_fuera(self):
        pass

    def test_calcular_recaudo_locales(self):
        

    def test_calcular_recaudo_horas_extra(self):
        pass

    def test_calcular_recaudo_mixto_local(self):
        pass


if __name__ == 'main':
    unittest.main()
