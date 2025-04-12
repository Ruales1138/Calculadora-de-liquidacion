import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.PaymentLogic import PaymentLogic_Calculator

def solicitar_dato(mensaje, tipo=float, positivo=True):
    """Solicita un dato al usuario y lo convierte al tipo especificado, validando su formato."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if positivo and valor < 0:
                raise ValueError("El valor no puede ser negativo.")
            return valor
        except ValueError:
            print(" Entrada inválida. Inténtelo de nuevo.")

def solicitar_fecha(mensaje):
    """Solicita una fecha y valida el formato correcto (DD/MM/YYYY)."""
    from datetime import datetime
    while True:
        fecha_str = input(mensaje)
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y").strftime("%d/%m/%Y")  # Asegurar formato correcto
        except ValueError:
            print(" Formato de fecha incorrecto. Use DD/MM/YYYY.")

def main():
    try:
        print("\n=== Calculadora de Liquidación Definitiva ===\n")
        
        # Solicitar datos con validaciones
        salario_base = solicitar_dato("Ingrese el salario base mensual: ")
        aux_transporte = solicitar_dato("Ingrese el auxilio de transporte: ")
        fecha_inicio = solicitar_fecha("Ingrese la fecha de inicio del contrato (DD/MM/YYYY): ")
        fecha_fin = solicitar_fecha("Ingrese la fecha de finalización del contrato (DD/MM/YYYY): ")
        dias_vacaciones_pend = solicitar_dato("Ingrese los días de vacaciones no gozadas: ")
        dias_prima = solicitar_dato("Ingrese los días de prima: ")
        dias_cesantias = solicitar_dato("Ingrese los días de cesantías: ")

        # Instanciar lógica de pago
        liquidacion = PaymentLogic_Calculator(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)

        # Mostrar resultados de manera ordenada
        print("\n=== Resumen de Liquidación ===\n")
        for clave, valor in liquidacion.resumen_liquidacion().items():
            print(f"{clave}: ${valor:,.2f}")

    except Exception as err:
        print(f"\n Error al calcular la liquidación: {err}")

if __name__ == "__main__":
    main()

    