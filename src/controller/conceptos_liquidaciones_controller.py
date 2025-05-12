import sys
sys.path.append( "src" )

import psycopg2

from model2.conceptos_liquidaciones import Conceptos_liquidaciones
import model2.SecretConfig as SecretConfig

class ControladorConceptosLiquidaciones :

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorConceptosLiquidaciones.ObtenerCursor()

        cursor.execute("""CREATE TABLE conceptos_liquidacion (
    id SERIAL PRIMARY KEY,
    liquidacion_id INT,
    concepto VARCHAR(100),
    monto DECIMAL(10,2),
    FOREIGN KEY (liquidacion_id) REFERENCES liquidaciones(id)
); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorConceptosLiquidaciones.ObtenerCursor()

        cursor.execute("""drop table usuarios""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarConceptosLiquidaciones( ConceptosLiquidaciones : Conceptos_liquidaciones ):
        """ Recibe un a instancia de la clase Conceptos_liquidaciones y la inserta en la tabla respectiva"""
        cursor = ControladorConceptosLiquidaciones.ObtenerCursor()
        cursor.execute( f"""insert into concepto_liquidaciones (id, liquidacion_id, concepto, 
                            monto) 
                        values ('{ConceptosLiquidaciones.id}', '{ConceptosLiquidaciones.liquidacion_id}', '{ConceptosLiquidaciones.concepto}',  
                            '{ConceptosLiquidaciones.monto}')""" )

        cursor.connection.commit()

    def BuscarUsuarioId( id ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = ControladorConceptosLiquidaciones.ObtenerCursor()

        cursor.execute(f"""select id, liquidacion_id, concepto, monto
        from conceptos_liquidaciones where id = '{id}'""" )
        fila = cursor.fetchone()
        resultado = Conceptos_liquidaciones( id=fila[0], liquidacion_id=fila[1], concepto=fila[2], monto=fila[3]  )
        return resultado

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor