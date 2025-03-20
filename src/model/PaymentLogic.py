from datetime import datetime

class PaymentLogic:
    def __init__(self, salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias):
        self.salario_base = salario_base
        self.aux_transporte = aux_transporte
        self.total_base = salario_base + aux_transporte
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        self.fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        self.dias_vacaciones_pend = dias_vacaciones_pend
        self.dias_prima = dias_prima
        self.dias_cesantias = dias_cesantias
        self.dias_trabajados = (self.fecha_fin - self.fecha_inicio).days

        if self.dias_trabajados <= 0:
            raise ValueError("Los días trabajados deben ser mayores a 0.")

    def calcular_anos_servicio(self):
        return self.dias_trabajados / 365.25

    def calcular_indemnizacion(self):
        return self.salario_base * self.calcular_anos_servicio()

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
        total = (
            self.calcular_indemnizacion() +
            self.calcular_vacaciones() +
            self.calcular_cesantias() +
            self.calcular_intereses_cesantias() +
            self.calcular_prima() +
            self.calcular_aguinaldo()
        )
        return total

