import model.LiquidationLogic as LiquidationLogic

# Obtener los datos de entrada
try:
    salary = float(input("Ingrese el salario mensual: "))
    days_worked = int(input("Ingrese los días trabajados: "))
    
    # Validaciones
    if salary <= 0 or days_worked <= 0:
        raise ValueError("El salario y los días trabajados deben ser valores positivos.")
    
    # Realizar el cálculo
    liquidation = LiquidationLogic.calcLiquidation(salary, days_worked)
    
    # Mostrar los datos de salida
    print(f"La liquidación calculada es: {liquidation}")
    
except Exception as err:
    print(f"Error al calcular la liquidación: {err}")
    
    