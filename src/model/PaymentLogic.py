from datetime import datetime

class PaymentLogic_Calculator:
    def __init__(self, salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias):
        self.salario_base = salario_base
        self.aux_transporte = aux_transporte
        self.total_base = salario_base + aux_transporte

        try:
            self.fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
            self.fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Las fechas deben estar en formato DD/MM/AAAA.")

        self.dias_vacaciones_pend = dias_vacaciones_pend
        self.dias_prima = dias_prima
        self.dias_cesantias = dias_cesantias
        self.dias_trabajados = (self.fecha_fin - self.fecha_inicio).days

        if self.dias_trabajados <= 0:
            raise ValueError("La fecha de fin debe ser posterior a la de inicio.")

    def calcular_anos_servicio(self):
        return self.dias_trabajados / 365.25

    def calcular_indemnizacion(self):
        anios = self.calcular_anos_servicio()
        if anios < 1:
            return self.salario_base  # Indemnización por menos de un año
        else:
            return self.salario_base + ((anios - 1) * (self.salario_base * 0.2))  # Ajuste para más años

    def calcular_vacaciones(self):
        return (self.salario_base / 30) * self.dias_vacaciones_pend

    def calcular_cesantias(self):
        return (self.total_base / 360) * self.dias_cesantias

    def calcular_intereses_cesantias(self):
        return self.calcular_cesantias() * 0.12

    def calcular_prima(self):
        return (self.total_base / 360) * self.dias_prima

    def calcular_aguinaldo(self):
        return self.salario_base / 12

    def calcular_total_liquidacion(self):
        return (
            self.calcular_indemnizacion() +
            self.calcular_vacaciones() +
            self.calcular_cesantias() +
            self.calcular_intereses_cesantias() +
            self.calcular_prima() +
            self.calcular_aguinaldo()
        )

    def resumen_liquidacion(self):
        return {
            "Días trabajados": self.dias_trabajados,
            "Años de servicio": round(self.calcular_anos_servicio(), 2),
            "Indemnización": round(self.calcular_indemnizacion(), 2),
            "Vacaciones": round(self.calcular_vacaciones(), 2),
            "Cesantías": round(self.calcular_cesantias(), 2),
            "Intereses cesantías": round(self.calcular_intereses_cesantias(), 2),
            "Prima": round(self.calcular_prima(), 2),
            "Aguinaldo": round(self.calcular_aguinaldo(), 2),
            "Total liquidación": round(self.calcular_total_liquidacion(), 2)
        }
    
class InvalidDateException(Exception):
    """Excepción personalizada para fechas inválidas en la liquidación."""
    pass



