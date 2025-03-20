import sys
sys.path.append("src")  

import unittest
from model.PaymentLogic import PaymentLogic  
  

class PaymentTest(unittest.TestCase):
    """
    Pruebas unitarias para la lógica de pago y liquidación definitiva
    """
    
    # ---- PRUEBAS PARA LIQUIDACIÓN ----
    def test_liquidacion_basica(self):
        """Prueba básica con valores correctos."""
        salario_base = 2000000
        aux_transporte = 140606
        fecha_inicio = "01/01/2023"  
        fecha_fin = "31/12/2023"
        dias_vacaciones_pend = 10
        dias_prima = 180
        dias_cesantias = 180
        
        logic = PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)
        resultado = logic.calcular_total_liquidacion()
        
        self.assertGreater(resultado, 0)

    def test_liquidacion_sin_aux_transporte(self):
        """Prueba con salario sin auxilio de transporte."""
        salario_base = 3000000
        aux_transporte = 0
        fecha_inicio = "01/06/2023"
        fecha_fin = "31/12/2023"
        dias_vacaciones_pend = 5
        dias_prima = 90
        dias_cesantias = 90
        
        logic = PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)
        resultado = logic.calcular_total_liquidacion()
        
        self.assertGreater(resultado, 0)

    def test_liquidacion_con_fechas_invalidas(self):
        """Prueba con fechas incorrectas (fecha fin antes de inicio)."""
        salario_base = 2000000
        aux_transporte = 140606
        fecha_inicio = "31/12/2023"
        fecha_fin = "01/01/2023"
        dias_vacaciones_pend = 10
        dias_prima = 180
        dias_cesantias = 180

        with self.assertRaises(ValueError):  # Corrección: ValueError en vez de InvalidDateException
            PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)

    def test_liquidacion_sin_derechos(self):
        """Prueba sin días de vacaciones, prima o cesantías."""
        salario_base = 2000000
        aux_transporte = 140606
        fecha_inicio = "01/06/2023"
        fecha_fin = "15/06/2023"
        dias_vacaciones_pend = 0
        dias_prima = 0
        dias_cesantias = 0
        
        logic = PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)
        resultado = logic.calcular_total_liquidacion()
        
        self.assertGreaterEqual(resultado, 0)  # Se cambia a `assertGreaterEqual` en caso de cálculos pequeños

    # ---- PRUEBAS PARA CÁLCULO DE PAGO ----
    def testPayment1(self):
        """Prueba con un salario de 2,000,000 y 180 días trabajados."""
        salario_base = 2000000
        aux_transporte = 0
        fecha_inicio = "01/01/2023"
        fecha_fin = "30/06/2023"
        
        logic = PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, 0, 180, 180)
        resultado = logic.calcular_total_liquidacion()
        
        self.assertGreater(resultado, 0)

    def testPayment2(self):
        """Prueba con un salario de 3,300,000 y 164 días trabajados, incluyendo indemnización."""
        salario_base = 3300000
        aux_transporte = 0
        fecha_inicio = "01/01/2023"
        fecha_fin = "14/06/2023"
        
        logic = PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, 0, 164, 164)
        resultado = logic.calcular_total_liquidacion()
        
        self.assertGreater(resultado, 0)

    def testPaymentExtraordinary1(self):
        """Prueba con salario alto (18,000,000) y 221 días trabajados."""
        salario_base = 18000000
        aux_transporte = 0
        fecha_inicio = "01/01/2023"
        fecha_fin = "10/08/2023"
        
        logic = PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, 0, 221, 221)
        resultado = logic.calcular_total_liquidacion()
        
        self.assertGreater(resultado, 0)

    def testPaymentExtraordinary2(self):
        """Prueba con salario alto (25,000,000) y 194 días trabajados."""
        salario_base = 25000000
        aux_transporte = 0
        fecha_inicio = "01/01/2023"
        fecha_fin = "14/07/2023"
        
        logic = PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, 0, 194, 194)
        resultado = logic.calcular_total_liquidacion()
        
        self.assertGreater(resultado, 0)


if __name__ == "__main__":
    unittest.main()


