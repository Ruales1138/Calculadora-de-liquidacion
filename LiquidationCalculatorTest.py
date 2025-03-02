import unittest
import LiquidationLogic

class TestLiquidationLogic(unittest.TestCase):
    
    def testLiquidation1(self):
        salary = 2000000
        days_worked = 180
        result = LiquidationLogic.calcLiquidation(salary, days_worked)
        expected = 2620000
        self.assertAlmostEqual(expected, result, 0)
    
    def testLiquidation2(self):
        salary = 3300000
        days_worked = 164
        result = LiquidationLogic.calcLiquidation(salary, days_worked)
        expected = 3938733  # Incluye indemnización
        self.assertAlmostEqual(expected, result, 0)
    
    def testLiquidationExtraordinary1(self):
        salary = 18000000
        days_worked = 221
        result = LiquidationLogic.calcLiquidation(salary, days_worked)
        expected = 28951000  # Incluye indemnización
        self.assertAlmostEqual(expected, result, 0)

    def testLiquidationExtraordinary2(self):
        salary = 25000000
        days_worked = 194
        result = LiquidationLogic.calcLiquidation(salary, days_worked)
        expected = 35297222  # Incluye indemnización
        self.assertAlmostEqual(expected, result, 0)

    def testLiquidationExtraordinary3(self):
        salary = 20000000
        days_worked = 214
        result = LiquidationLogic.calcLiquidation(salary, days_worked)
        expected = 31148888  # Incluye indemnización
        self.assertAlmostEqual(expected, result, delta=1)

    def testLiquidationZeroDays(self):
        salary = 2500000
        days_worked = 0

        with self.assertRaises(ValueError):
            LiquidationLogic.calcLiquidation(salary, days_worked)
    

    def testNegativeSalary(self):
        salary = -2000000
        days_worked = 100
        
        with self.assertRaises(ValueError):
            LiquidationLogic.calcLiquidation(salary, days_worked)
    

    def testNegativeDaysWorked(self):
        salary = 2500000
        days_worked = -50
        
        with self.assertRaises(ValueError):
            LiquidationLogic.calcLiquidation(salary, days_worked)

if __name__ == "__main__":
    unittest.main()