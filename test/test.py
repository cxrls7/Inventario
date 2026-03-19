import unittest
# Importamos las funciones desde tu carpeta src
from src.inventario import calcular_estadisticas

class TestSistemaInventario(unittest.TestCase):

    def setUp(self):
        
        self.inventario_vacio = []
        self.inventario_con_datos = [
            {"nombre": "Laptop", "precio": 2000000, "cantidad": 2}, 
            {"nombre": "Mouse", "precio": 50000, "cantidad": 5},     
            {"nombre": "Teclado", "precio": 150000, "cantidad": 3}   
        ]

    def test_flujo_estadisticas_exitoso(self):
        """Prueba que el cálculo matemático sea exacto"""
    
        unidades, total_dinero = calcular_estadisticas(self.inventario_con_datos)
        
      
        self.assertEqual(unidades, 10, "La suma de unidades debería ser 10")
        self.assertEqual(total_dinero, 4700000, "El valor total debería ser 4.700.000")

    def test_resiliencia_inventario_vacio(self):
        """Prueba que el sistema no se rompa (NoneType error) si no hay datos"""
        unidades, total_dinero = calcular_estadisticas(self.inventario_vacio)
        
        self.assertEqual(unidades, 0)
        self.assertEqual(total_dinero, 0)
        self.assertIsInstance(unidades, int)

    def test_tipos_de_datos(self):
        """Prueba que los resultados siempre sean numéricos (evitar errores de formato)"""
        total_dinero = calcular_estadisticas(self.inventario_con_datos)
        
        self.assertTrue(isinstance(total_dinero, (int, float)), "El total debe ser un número")
        self.assertGreater(total_dinero, 0, "El valor total debe ser mayor a cero si hay productos")

if __name__ == '__main__':
    unittest.main()
