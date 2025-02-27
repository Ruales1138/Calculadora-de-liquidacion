class LiquidationLogic:
    @staticmethod
    def calcLiquidation(salary, days_worked):
        """
        Calcula la liquidación definitiva de un empleado.

        salary: Salario mensual del empleado.
        days_worked: Número de días trabajados.
        Total de la liquidación.
        """

        # Validaciones de entrada
        if salary < 0 or days_worked < 0:
            raise ValueError("Salary and days worked must be non-negative.")

        # Cálculo de componentes de la liquidación
        prima = (salary / 360) * days_worked * 30  # Prima de servicios
        cesantias = (salary / 360) * days_worked  # Cesantías
        intereses_cesantias = cesantias * 0.12  # Intereses sobre cesantías (12%)
        vacaciones = (salary / 720) * days_worked  # Vacaciones proporcionales

        # Total de la liquidación
        total_liquidation = prima + cesantias + intereses_cesantias + vacaciones

        return round(total_liquidation, 2)