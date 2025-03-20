from model.PaymentLogic import PaymentLogic

try:
    # Solicitar datos de entrada al usuario
    salario_base = float(input("Ingrese el salario base mensual: "))
    aux_transporte = float(input("Ingrese el auxilio de transporte: "))
    fecha_inicio = input("Ingrese la fecha de inicio del contrato (DD/MM/YYYY): ")
    fecha_fin = input("Ingrese la fecha de finalización del contrato (DD/MM/YYYY): ")
    dias_vacaciones_pend = float(input("Ingrese los días de vacaciones no gozadas: "))
    dias_prima = float(input("Ingrese los días de prima: "))
    dias_cesantias = float(input("Ingrese los días de cesantías: "))

    # Validaciones de entrada
    if salario_base <= 0 or aux_transporte < 0 or dias_vacaciones_pend < 0 or dias_prima < 0 or dias_cesantias < 0:
        raise ValueError("Los valores ingresados deben ser positivos.")

    # Crear instancia de PaymentLogic y calcular la liquidación
    liquidacion = PaymentLogic(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)

    # Mostrar resultados
    print("\n--- Resultados de la Liquidación ---")
    print(f"Indemnización por despido: ${liquidacion.calcular_indemnizacion():,.2f}")
    print(f"Vacaciones no gozadas: ${liquidacion.calcular_vacaciones():,.2f}")
    print(f"Cesantías: ${liquidacion.calcular_cesantias():,.2f}")
    print(f"Intereses sobre cesantías: ${liquidacion.calcular_intereses_cesantias():,.2f}")
    print(f"Prima: ${liquidacion.calcular_prima():,.2f}")
    print(f"Aguinaldo: ${liquidacion.calcular_aguinaldo():,.2f}")
    print(f"\nTotal de la liquidación definitiva: ${liquidacion.calcular_total_liquidacion():,.2f}")

except Exception as err:
    print(f"Error al calcular la liquidación: {err}")
    