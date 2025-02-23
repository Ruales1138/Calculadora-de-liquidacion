import unittest
from liquidation_logic import LiquidationLogic

class TestLiquidationLogic(unittest.TestCase):
    
    def testLiquidation1(self):
        #Datos de entrada
        salary = 2000000
        days_worked = 180

        #Proceso
        result = LiquidationLogic.calcLiquidation(salary, days_worked)

        #Datos de salida esperados
        expected = round((salary * 0.0833) + ((salary / 360) * days_worked) + ((salary / 720) * days_worked) + (((salary / 360) * days_worked) * 0.12), 2)

        #Prueba
        self.assertAlmostEqual(expected, result, 2)
    
    def testLiquidation2(self):
        salary = 3300000
        days_worked = 164

        result = LiquidationLogic.calcLiquidation(salary, days_worked)

        expected = round((salary * 0.0833) + ((salary / 360) * days_worked) + ((salary / 720) * days_worked) + (((salary / 360) * days_worked) * 0.12), 2)
        
        self.assertAlmostEqual(expected, result, 2)
    
    def testLiquidation3(self):
        salary = 2000000
        days_worked = 539

        result = LiquidationLogic.calcLiquidation(salary, days_worked)

        expected = round((salary * 0.0833) + ((salary / 360) * days_worked) + ((salary / 720) * days_worked) + (((salary / 360) * days_worked) * 0.12), 2)
        
        self.assertAlmostEqual(expected, result, 2)

    def testLiquidationZeroDays(self):
        salary = 2500000
        days_worked = 0
        result = LiquidationLogic.calcLiquidation(salary, days_worked)
        expected = round((salary * 0.0833), 2)
        self.assertAlmostEqual(expected, result, 2)
    
    def testNegativeSalary(self):
        salary = -2000000
        days_worked = 100
        self.assertRaises(ValueError, LiquidationLogic.calcLiquidation, salary, days_worked)
    
    def testNegativeDaysWorked(self):
        salary = 2500000
        days_worked = -50
        self.assertRaises(ValueError, LiquidationLogic.calcLiquidation, salary, days_worked)

if __name__ == "__main__":
    unittest.main()