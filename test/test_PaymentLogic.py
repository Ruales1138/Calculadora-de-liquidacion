import sys
sys.path.append("src")  # Permitir acceso a los módulos en src

import unittest
from model.PaymentLogic import calcular_total_liquidacion, calcPayment, InvalidDateException


class PaymentTest(unittest.TestCase):
    """
    Pruebas unitarias para la lógica de pago y liquidación definitiva
    """
    
    # ---- PRUEBAS PARA LIQUIDACIÓN ----
    def test_liquidacion_basica(self):
        """Prueba básica con valores correctos."""
        salario_base = 2000000
        aux_transporte = 140606
        fecha_inicio = "2023-01-01"
        fecha_fin = "2023-12-31"
        dias_vacaciones_pend = 10
        dias_prima = 180
        dias_cesantias = 180
        resultado = calcular_liquidacion(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)
        self.assertIn("total_liquidacion", resultado)
        self.assertGreater(resultado["total_liquidacion"], 0)

    def test_liquidacion_sin_aux_transporte(self):
        """Prueba con salario sin auxilio de transporte."""
        salario_base = 3000000
        aux_transporte = 0
        fecha_inicio = "2023-06-01"
        fecha_fin = "2023-12-31"
        dias_vacaciones_pend = 5
        dias_prima = 90
        dias_cesantias = 90
        resultado = calcular_liquidacion(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)
        self.assertGreater(resultado["total_liquidacion"], 0)
    
    def test_liquidacion_con_fechas_invalidas(self):
        """Prueba con fechas incorrectas (fecha fin antes de inicio)."""
        salario_base = 2000000
        aux_transporte = 140606
        fecha_inicio = "2023-12-31"
        fecha_fin = "2023-01-01"
        dias_vacaciones_pend = 10
        dias_prima = 180
        dias_cesantias = 180
        with self.assertRaises(InvalidDateException):
            calcular_liquidacion(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)

    def test_liquidacion_sin_derechos(self):
        """Prueba sin días de vacaciones, prima o cesantías."""
        salario_base = 2000000
        aux_transporte = 140606
        fecha_inicio = "2023-06-01"
        fecha_fin = "2023-06-15"
        dias_vacaciones_pend = 0
        dias_prima = 0
        dias_cesantias = 0
        resultado = calcular_liquidacion(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)
        self.assertEqual(resultado["total_liquidacion"], 0)

    # ---- PRUEBAS PARA CÁLCULO DE PAGO ----
    def testPayment1(self):
        """Prueba con un salario de 2,000,000 y 180 días trabajados."""
        salario_base = 2000000
        dias_trabajados = 180
        self.assertAlmostEqual(calcPayment(salario_base, dias_trabajados), 2620000, 0)
    
    def testPayment2(self):
        """Prueba con un salario de 3,300,000 y 164 días trabajados, incluyendo indemnización."""
        salario_base = 3300000
        dias_trabajados = 164
        self.assertAlmostEqual(calcPayment(salario_base, dias_trabajados), 3938733, 0)
    
    def testPaymentExtraordinary1(self):
        """Prueba con salario alto (18,000,000) y 221 días trabajados."""
        salario_base = 18000000
        dias_trabajados = 221
        self.assertAlmostEqual(calcPayment(salario_base, dias_trabajados), 28951000, 0)

    def testPaymentExtraordinary2(self):
        """Prueba con salario alto (25,000,000) y 194 días trabajados."""
        salario_base = 25000000
        dias_trabajados = 194
        self.assertAlmostEqual(calcPayment(salario_base, dias_trabajados), 35297222, 0)

    def testPaymentExtraordinary3(self):
        """Prueba con salario alto (20,000,000) y 214 días trabajados."""
        salario_base = 20000000
        dias_trabajados = 214
        self.assertAlmostEqual(calcPayment(salario_base, dias_trabajados), 31148888, delta=1)

    def testPaymentZeroDays(self):
        """Prueba con 0 días trabajados, debería lanzar un ValueError."""
        salario_base = 2500000
        dias_trabajados = 0
        with self.assertRaises(ValueError):
            calcPayment(salario_base, dias_trabajados)
    
    def testNegativeSalary(self):
        """Prueba con salario negativo, debería lanzar un ValueError."""
        salario_base = -2000000
        dias_trabajados = 100
        with self.assertRaises(ValueError):
            calcPayment(salario_base, dias_trabajados)
    
    def testNegativeDaysWorked(self):
        """Prueba con días trabajados negativos, debería lanzar un ValueError."""
        salario_base = 2500000
        dias_trabajados = -50
        with self.assertRaises(ValueError):
            calcPayment(salario_base, dias_trabajados)

if __name__ == "__main__":
    unittest.main()
