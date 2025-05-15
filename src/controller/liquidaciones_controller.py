import sys
sys.path.append("src")

import psycopg2
from model2.liquidacion import Liquidacion
import SecretConfig


class ControladorLiquidaciones:

    @staticmethod
    def CrearTabla():
        """ Crea la tabla de liquidaciones en la base de datos """
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS liquidaciones (
                id SERIAL PRIMARY KEY,
                salario_base NUMERIC(12, 2) NOT NULL,
                aux_transporte NUMERIC(12, 2) NOT NULL,
                fecha_inicio DATE NOT NULL,
                fecha_fin DATE NOT NULL,
                dias_trabajados INTEGER NOT NULL,
                anos_servicio NUMERIC(5, 2) NOT NULL,
                dias_vacaciones_pend INTEGER NOT NULL,
                dias_prima INTEGER NOT NULL,
                dias_cesantias INTEGER NOT NULL,
                indemnizacion NUMERIC(12, 2) NOT NULL,
                vacaciones NUMERIC(12, 2) NOT NULL,
                cesantias NUMERIC(12, 2) NOT NULL,
                intereses_cesantias NUMERIC(12, 2) NOT NULL,
                prima NUMERIC(12, 2) NOT NULL,
                aguinaldo NUMERIC(12, 2) NOT NULL,
                total_liquidacion NUMERIC(14, 2) NOT NULL,
                fecha_calculo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cursor.connection.commit()

    @staticmethod
    def EliminarTabla():
        """ Elimina la tabla de liquidaciones """
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("DROP TABLE IF EXISTS liquidaciones;")
        cursor.connection.commit()

    @staticmethod
    def InsertarLiquidacion(liquidacion: Liquidacion):
        """ Inserta una liquidación en la base de datos """
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("""
            INSERT INTO liquidaciones (
                salario_base, aux_transporte, fecha_inicio, fecha_fin,
                dias_trabajados, anos_servicio, dias_vacaciones_pend,
                dias_prima, dias_cesantias, indemnizacion, vacaciones,
                cesantias, intereses_cesantias, prima, aguinaldo,
                total_liquidacion, fecha_calculo
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            liquidacion.salario_base,
            liquidacion.aux_transporte,
            liquidacion.fecha_inicio,
            liquidacion.fecha_fin,
            liquidacion.dias_trabajados,
            liquidacion.anos_servicio,
            liquidacion.dias_vacaciones_pend,
            liquidacion.dias_prima,
            liquidacion.dias_cesantias,
            liquidacion.indemnizacion,
            liquidacion.vacaciones,
            liquidacion.cesantias,
            liquidacion.intereses_cesantias,
            liquidacion.prima,
            liquidacion.aguinaldo,
            liquidacion.total_liquidacion,
            liquidacion.fecha_calculo
        ))
        id_insertado = cursor.fetchone()[0]
        cursor.connection.commit()
        return id_insertado

    @staticmethod
    def BuscarPorId(id):
        """ Busca una liquidación por ID y retorna un objeto Liquidacion """
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("""
            SELECT id, salario_base, aux_transporte, fecha_inicio, fecha_fin,
                   dias_trabajados, anos_servicio, dias_vacaciones_pend,
                   dias_prima, dias_cesantias, indemnizacion, vacaciones,
                   cesantias, intereses_cesantias, prima, aguinaldo,
                   total_liquidacion, fecha_calculo
            FROM liquidaciones
            WHERE id = %s
        """, (id,))
        fila = cursor.fetchone()
        if fila:
            return Liquidacion(
                id=fila[0],
                salario_base=fila[1],
                aux_transporte=fila[2],
                fecha_inicio=fila[3],
                fecha_fin=fila[4],
                dias_trabajados=fila[5],
                anos_servicio=fila[6],
                dias_vacaciones_pend=fila[7],
                dias_prima=fila[8],
                dias_cesantias=fila[9],
                indemnizacion=fila[10],
                vacaciones=fila[11],
                cesantias=fila[12],
                intereses_cesantias=fila[13],
                prima=fila[14],
                aguinaldo=fila[15],
                total_liquidacion=fila[16],
                fecha_calculo=fila[17]
            )
        return None

    @staticmethod
    def ObtenerCursor():
        """ Retorna un cursor activo conectado a la base de datos PostgreSQL """
        connection = psycopg2.connect(
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            host=SecretConfig.PGHOST,
            port=SecretConfig.PGPORT
        )
        return connection.cursor()
