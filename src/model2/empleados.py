from datetime import date

class Empleado:

    def __init__( self, id, nombre, apellido, cedula, fecha_ingreso, salario, cargo )  :
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_ingreso = fecha_ingreso
        self.salario = salario
        self.cargo = cargo


    def esIgual( self, liquidar_con ) :

        assert( self.id == liquidar_con.id )
        assert( self.nombre == liquidar_con.nombre )
        assert( self.apellido== liquidar_con.apellido )
        assert( self.cedula== liquidar_con.cedula )
        assert( self.fecha_ingreso== liquidar_con.fecha_ingreso )
        assert( self.salario== liquidar_con.salario )
        assert( self.cargo== liquidar_con.cargo )