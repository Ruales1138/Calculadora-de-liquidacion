import sys
sys.path.append( "src" )

import psycopg2

from model2.historial_salarios import Historial_salarios
import SecretConfig as SecretConfig

class ControladorHistorialSalarios :

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorHistorialSalarios.ObtenerCursor()

        cursor.execute("""CREATE TABLE historial_salarios (
    id SERIAL PRIMARY KEY,
    empleado_id INT,
    salario DECIMAL(10,2),
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)
); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorHistorialSalarios.ObtenerCursor()

        cursor.execute("""drop table usuarios""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarHistorialSalarios( HistorialSalarios : Historial_salarios):
        """ Recibe un a instancia de la clase Conceptos_liquidaciones y la inserta en la tabla respectiva"""
        cursor = ControladorHistorialSalarios.ObtenerCursor()
        cursor.execute( f"""insert into usuarios (id, empleado_id, salario, 
                            monto) 
                        values ('{HistorialSalarios.id}', '{HistorialSalarios.empleado_id}', '{HistorialSalarios.salario}',  
                            '{HistorialSalarios.fecha_inicio}', '{HistorialSalarios.fecha_fin}')""" )

        cursor.connection.commit()

    def BuscarEmpleadoId( empleado_id ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = ControladorHistorialSalarios.ObtenerCursor()

        cursor.execute(f"""select id, liquidacion_id, concepto, monto
        from historial_salarios where empleado_id = '{empleado_id}'""" )
        fila = cursor.fetchone()
        resultado = ControladorHistorialSalarios( id=fila[0], empleado_id=fila[1], salario=fila[2], fecha_inicio=fila[3],  fecha_fin=fila[4])
        return resultado

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor