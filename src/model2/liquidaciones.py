import datetime
class Liquidaciones :
    
    def __init__(self, id : str ,
  empleado_id : str,
  fecha_salida : str,
  fecha_calculo : str,
  dias_trabajados : datetime,
  total_liquidacion : float):
        
        self.id = id
        self.empleado_id = empleado_id
        self.fecha_salida = fecha_salida
        self.fecha_calculo = fecha_calculo
        self.dias_trabajados = dias_trabajados
        self.total_liquidacion = total_liquidacion

    def EsIgual( self, otro ):
        
        assert( self.id == otro.id )
        assert( self.empleado_id == otro.empleado_id)
        assert( self.fecha_salida == otro.fecha_salida)
        assert( self.fecha_calculo == otro.fecha_calculo)
        assert( self.dias_trabajados == otro.dias_trabajados)
        assert( self.total_liquidacion == otro.total_liquidacion)
        
        return True