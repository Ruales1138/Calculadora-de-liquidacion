import datetime
class Historial_salarios :
    
    def __init__(self, id : str ,
  empleado_id : str,
  salario : str,
  fecha_inicio : datetime,
  fecha_fin : datetime):
        
        self.id = id
        self.empleado_id = empleado_id
        self.salario = salario
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def EsIgual( self, otro ):
        
        assert( self.id == otro.id )
        assert( self.empleado_id == otro.empleado_id)
        assert( self.salario == otro.salario)
        assert( self.fecha_inicio == otro.fecha_inicio)
        assert( self.fecha_fin == otro.fecha_fin)
        
        return True