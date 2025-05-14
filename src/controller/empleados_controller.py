import sys
sys.path.append( "src" )

import psycopg2

from model2.empleados import Empleado
import model2.SecretConfig as SecretConfig

class ControladorEmpleado :

    def CrearTabla():
        cursor = ControladorEmpleado.ObtenerCursor()

        cursor.execute("""CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    cedula VARCHAR(20) UNIQUE,
    fecha_ingreso DATE,
    salario DECIMAL(10,2),
    cargo VARCHAR(100)
); """)
        cursor.connection.commit()

    
    def EliminarTabla():
        """ Borra la tabla empleados y sus dependencias """
        cursor = ControladorEmpleado.ObtenerCursor()
        cursor.execute("""DROP TABLE IF EXISTS empleados CASCADE""")
        cursor.connection.commit()


    def InsertarEmpleado( empleado : Empleado ):
        """ Recibe un a instancia de la clase Empleado y la inserta en la tabla respectiva"""
        cursor = ControladorEmpleado.ObtenerCursor()
        cursor.execute( f"""insert into usuarios (id, nombre, apellido, 
                            cedula, fecha_ingreso, 
                            salario, cargo) 
                        values ('{empleado.id}', '{empleado.nombre}', '{empleado.apellido}',  
                            '{empleado.cedula}', '{empleado.fecha_ingreso}',
                            '{empleado.salario}', '{empleado.cargo}""" )

        cursor.connection.commit()

    def BuscarEmpleadoId( id ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = ControladorEmpleado.ObtenerCursor()

        cursor.execute(f"""select id, nombre, apellido, cedula, fecha_ingreso, salario, cargo
        from empleados where id = '{id}'""" )
        fila = cursor.fetchone()
        resultado = Empleado ( id=fila[0], nombre=fila[1], apellido=fila[2], cedula=fila[3], fecha_ingreso=fila[4], salario=fila[5],cargo=fila[6]  )
        return resultado
    
    def ActualizarEmpleado(empleado: Empleado):
        cursor = ControladorEmpleado.ObtenerCursor()
        cursor.execute("""
            UPDATE empleados 
            SET nombre=%s, apellido=%s, cedula=%s, fecha_ingreso=%s, salario=%s, cargo=%s
            WHERE id=%s
        """, (empleado.nombre, empleado.apellido, empleado.cedula, empleado.fecha_ingreso, empleado.salario, empleado.cargo, empleado.id))
        cursor.connection.commit()


    def ObtenerCursor():
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor