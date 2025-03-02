def calcLiquidation(salary, days_worked):
    # Validaciones de entrada
    if salary <= 0 or days_worked <= 0:
        raise ValueError("Salary and days worked must not be zero or negative values.")

    # Cálculo de componentes de la liquidación
    prima = (salary * days_worked) / 360  # Prima de servicios
    cesantias = (salary * days_worked) / 360  # Cesantías
    intereses_cesantias = cesantias * 0.12  # Intereses sobre cesantías (12%)
    vacaciones = (salary * days_worked) / 720  # Vacaciones proporcionales

    # Total de la liquidación
    total_liquidation = prima + cesantias + intereses_cesantias + vacaciones

    return round(total_liquidation)

