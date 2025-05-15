from datetime import datetime

class Liquidacion:
    def __init__(self, id, salario_base, aux_transporte, fecha_inicio, fecha_fin,
                 dias_trabajados, anos_servicio, dias_vacaciones_pend, dias_prima,
                 dias_cesantias, indemnizacion, vacaciones, cesantias,
                 intereses_cesantias, prima, aguinaldo, total_liquidacion,
                 fecha_calculo):
        self.id = id
        self.salario_base = salario_base
        self.aux_transporte = aux_transporte
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.dias_trabajados = dias_trabajados
        self.anos_servicio = anos_servicio
        self.dias_vacaciones_pend = dias_vacaciones_pend
        self.dias_prima = dias_prima
        self.dias_cesantias = dias_cesantias
        self.indemnizacion = indemnizacion
        self.vacaciones = vacaciones
        self.cesantias = cesantias
        self.intereses_cesantias = intereses_cesantias
        self.prima = prima
        self.aguinaldo = aguinaldo
        self.total_liquidacion = total_liquidacion
        self.fecha_calculo = fecha_calculo

    def esIgual(self, comparar_con):
        assert self.id == comparar_con.id
        assert self.salario_base == comparar_con.salario_base
        assert self.aux_transporte == comparar_con.aux_transporte
        assert self.fecha_inicio == comparar_con.fecha_inicio
        assert self.fecha_fin == comparar_con.fecha_fin
        assert self.dias_trabajados == comparar_con.dias_trabajados
        assert self.anos_servicio == comparar_con.anos_servicio
        assert self.dias_vacaciones_pend == comparar_con.dias_vacaciones_pend
        assert self.dias_prima == comparar_con.dias_prima
        assert self.dias_cesantias == comparar_con.dias_cesantias
        assert self.indemnizacion == comparar_con.indemnizacion
        assert self.vacaciones == comparar_con.vacaciones
        assert self.cesantias == comparar_con.cesantias
        assert self.intereses_cesantias == comparar_con.intereses_cesantias
        assert self.prima == comparar_con.prima
        assert self.aguinaldo == comparar_con.aguinaldo
        assert self.total_liquidacion == comparar_con.total_liquidacion
        assert self.fecha_calculo == comparar_con.fecha_calculo
