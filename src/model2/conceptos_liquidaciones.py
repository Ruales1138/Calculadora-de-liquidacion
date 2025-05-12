
class Conceptos_liquidaciones :
    
    def __init__(self, id : str ,
  liquidacion_id : str,
  concepto : str,
  monto : str):
        
        self.id = id
        self.liquidacion_id = liquidacion_id
        self.concepto = concepto
        self.monto = monto

    def EsIgual( self, otro ):
        
        assert( self.id == otro.id )
        assert( self.liquidacion_id == otro.liquidacion_id)
        assert( self.concepto == otro.concepto)
        assert( self.monto == otro.monto)
        
        return True