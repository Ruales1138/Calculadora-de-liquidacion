class LiquidationLogic:
    @staticmethod
    def calcLiquidation(salary, days_worked):
        if salary < 0 or days_worked < 0:
            raise ValueError("Salary and days worked must be non-negative.")
        
        bonus = salary * 0.0833  # Prima de servicios (aprox. 8.33%)
        severance = (salary / 360) * days_worked  # Cesantías
        vacations = (salary / 720) * days_worked  # Vacaciones proporcionales
        severance_interest = severance * 0.12  # Intereses sobre cesantías (12%)
        
        total_liquidation = bonus + severance + vacations + severance_interest
        return round(total_liquidation, 2)