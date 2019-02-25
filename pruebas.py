import unittest
import funciones as f

class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):
        self.assertEqual(f.calcular_precio_producto(1000), 1500)
        self.assertEqual(f.calcular_precio_producto(0), 0)

    def test_calcular_precio_servicio(self):
        pass

    def test_calcular_precio_servicio_extras(self):
        self.assertEqual(f.calcular_precio_servicio_extras(6), 750000.0)
        self.assertEqual(f.calcular_precio_servicio_extras(10), 1250000.0)

    def test_calcular_costo_envio(self):
        pass

    def test_calcular_precio_producto_fuera(self):
        self.assertEqual(f.calcular_precio_producto_fuera(1000, 4), 1960)
        self.assertEqual(f.calcular_precio_producto_fuera(2000, 6), 3690)

    def test_calcular_iva_producto(self):
        pass

    def test_calcular_iva_servicio(self):
        self.assertEqual(f.calcular_iva_servicio(3, 0.19), 57000)
        self.assertEqual(f.calcular_iva_servicio(2, 0.16), 32000)

    def test_calcular_iva_envio(self):
        pass

    def test_calcular_iva_servicio_fuera(self):
        pass

    def test_calcular_recaudo_locales(self):
        pass

    def test_calcular_recaudo_horas_extra(self):
        pass

    def test_calcular_recaudo_mixto_local(self):
        pass


if __name__ == 'main':
    unittest.main()
