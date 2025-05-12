import sys
sys.path.append( "src" )

import psycopg2

from model2.liquidaciones import Liquidaciones
import model2.SecretConfig as SecretConfig

class Controladorliquidaciones:

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = Controladorliquidaciones.ObtenerCursor()

        cursor.execute("""CREATE TABLE liquidaciones (
    id SERIAL PRIMARY KEY,
    empleado_id INT,
    fecha_salida DATE,
    fecha_calculo DATE,
    dias_trabajados INT,
    total_liquidacion DECIMAL(12,2),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)
); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = Controladorliquidaciones.ObtenerCursor()

        cursor.execute("""drop table usuarios""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarLiquidaciones( Liquidaciones : Liquidaciones):
        """ Recibe un a instancia de la clase Liquidaciones y la inserta en la tabla respectiva"""
        cursor = Controladorliquidaciones.ObtenerCursor()
        cursor.execute( f"""insert into liquidaciones (id, empleado_id, fecha_salida, fecha_calculo, dias_trabajados, 
                            total_liquidacion) 
                        values ('{Liquidaciones.id}', '{Liquidaciones.empleado_id}', '{Liquidaciones.fecha_salida}',  
                            '{Liquidaciones.fecha_calculo}', '{Liquidaciones.dias_trabajados}', '{Liquidaciones.total_liquidacion}')""" )

        cursor.connection.commit()

    def BuscarId( id ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = Controladorliquidaciones.ObtenerCursor()

        cursor.execute(f"""select id, empleado_id, fecha_salida, fecha_calculo, dias_trabajados, total_liquidacion
        from liquidaciones where id = '{id}'""" )
        fila = cursor.fetchone()
        resultado = Controladorliquidaciones( id=fila[0], empleado_id=fila[1], fecha_salida=fila[2], fecha_calculo=fila[3],  dias_trabajados=fila[4], total_liquidacion=fila[5])
        return resultado

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor