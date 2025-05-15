import sys
sys.path.append("src")

import psycopg2
from model2.liquidaciones import Liquidacion
import SecretConfig

class ControladorLiquidaciones:

    @staticmethod
    def CrearTabla():
        """ Crea la tabla de liquidaciones en la base de datos """
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS liquidaciones (
                id SERIAL PRIMARY KEY,
                nombre_empleado VARCHAR(100) NOT NULL,
                cedula_empleado VARCHAR(20) NOT NULL,
                fecha_ingreso DATE NOT NULL,
                fecha_salida DATE NOT NULL,
                salario_base NUMERIC(15, 2) NOT NULL,
                dias_laborados INTEGER NOT NULL,
                total_liquidacion NUMERIC(15, 2) NOT NULL,
                fecha_calculo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cursor.connection.commit()

    @staticmethod
    def EliminarTabla():
        """ Elimina la tabla de liquidaciones de la base de datos """
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("DROP TABLE IF EXISTS liquidaciones")
        cursor.connection.commit()

    @staticmethod
    def InsertarLiquidacion(liquidacion: Liquidacion):
        """ Inserta una liquidación en la tabla """
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("""
            INSERT INTO liquidaciones (
                nombre_empleado,
                cedula_empleado,
                fecha_ingreso,
                fecha_salida,
                salario_base,
                dias_laborados,
                total_liquidacion,
                fecha_calculo
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            liquidacion.nombre_empleado,
            liquidacion.cedula_empleado,
            liquidacion.fecha_ingreso,
            liquidacion.fecha_salida,
            liquidacion.salario_base,
            liquidacion.dias_laborados,
            liquidacion.total_liquidacion,
            liquidacion.fecha_calculo
        ))
        id_insertado = cursor.fetchone()[0]
        cursor.connection.commit()
        return id_insertado

    @staticmethod
    def BuscarPorId(id):
        """ Busca una liquidación por su ID y retorna un objeto Liquidacion """
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("""
            SELECT id, nombre_empleado, cedula_empleado, fecha_ingreso,
                   fecha_salida, salario_base, dias_laborados,
                   total_liquidacion, fecha_calculo
            FROM liquidaciones
            WHERE id = %s
        """, (id,))
        fila = cursor.fetchone()
        if fila:
            return Liquidacion(
                id=fila[0],
                nombre_empleado=fila[1],
                cedula_empleado=fila[2],
                fecha_ingreso=fila[3],
                fecha_salida=fila[4],
                salario_base=fila[5],
                dias_laborados=fila[6],
                total_liquidacion=fila[7],
                fecha_calculo=fila[8]
            )
        return None

    @staticmethod
    def ObtenerCursor():
        """ Crea la conexión a la base de datos y retorna un cursor """
        connection = psycopg2.connect(
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            host=SecretConfig.PGHOST,
            port=SecretConfig.PGPORT
        )
        return connection.cursor()