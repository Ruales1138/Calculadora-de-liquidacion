from datetime import datetime

class Liquidacion:
    def __init__(self, id, nombre_empleado, cedula_empleado, fecha_ingreso, fecha_salida,
                 salario_base, dias_laborados, total_liquidacion, fecha_calculo):
        self.id = id
        self.nombre_empleado = nombre_empleado
        self.cedula_empleado = cedula_empleado
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.salario_base = salario_base
        self.dias_laborados = dias_laborados
        self.total_liquidacion = total_liquidacion
        self.fecha_calculo = fecha_calculo

    def esIgual(self, comparar_con):
        assert self.id == comparar_con.id
        assert self.nombre_empleado == comparar_con.nombre_empleado
        assert self.cedula_empleado == comparar_con.cedula_empleado
        assert self.fecha_ingreso == comparar_con.fecha_ingreso
        assert self.fecha_salida == comparar_con.fecha_salida
        assert self.salario_base == comparar_con.salario_base
        assert self.dias_laborados == comparar_con.dias_laborados
        assert self.total_liquidacion == comparar_con.total_liquidacion
        assert self.fecha_calculo == comparar_con.fecha_calculo