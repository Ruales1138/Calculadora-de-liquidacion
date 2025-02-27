import LiquidationLogic

# Obtener los datos de entrada
try:
    salary = float(input("Ingrese el salario mensual del empleado: "))
    days_worked = int(input("Ingrese el número de días trabajados: "))
    
    # Realizar el proceso
    liquidation = LiquidationLogic.calcLiquidation(salary, days_worked)
    
    # Mostrar los datos de salida
    print(f"El valor de la liquidación es: {liquidation}")
except Exception as err:
    print(f"Error al calcular la liquidación: {err}")
    