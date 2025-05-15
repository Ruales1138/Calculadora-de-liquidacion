import unittest
import sys
import os
from datetime import datetime, timedelta

sys.path.append("src")
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.controller.liquidaciones_controller import ControladorLiquidaciones
from src.model2.liquidacion import Liquidacion

class LiquidacionesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ControladorLiquidaciones.EliminarTabla()
        ControladorLiquidaciones.CrearTabla()

        cls.ids = []
        base_date = datetime(2023, 1, 1)

        # Crear y guardar 3 liquidaciones
        for i in range(3):
            liquidacion = Liquidacion(
                id=None,
                salario_base=1500000 + i * 100000,
                aux_transporte=140606,
                fecha_inicio=base_date,
                fecha_fin=base_date + timedelta(days=365),
                dias_trabajados=365,
                anos_servicio=1.0,
                dias_vacaciones_pend=5 + i,
                dias_prima=180,
                dias_cesantias=180,
                indemnizacion=1500000 + i * 100000,
                vacaciones=250000,
                cesantias=400000,
                intereses_cesantias=48000,
                prima=400000,
                aguinaldo=125000,
                total_liquidacion=3725000 + i * 100000,
                fecha_calculo=datetime.now()
            )
            inserted_id = ControladorLiquidaciones.InsertarLiquidacion(liquidacion)
            cls.ids.append(inserted_id)

    # -------------------- Pruebas de Inserción --------------------
    def test_insertar_liquidacion_1(self):
        self.assertIsInstance(self.ids[0], int)

    def test_insertar_liquidacion_2(self):
        self.assertIsInstance(self.ids[1], int)

    def test_insertar_liquidacion_3(self):
        self.assertIsInstance(self.ids[2], int)

    # -------------------- Pruebas de Búsqueda --------------------
    def test_buscar_liquidacion_1(self):
        buscado = ControladorLiquidaciones.BuscarPorId(self.ids[0])
        self.assertIsNotNone(buscado)
        self.assertEqual(buscado.dias_vacaciones_pend, 5)

    def test_buscar_liquidacion_2(self):
        buscado = ControladorLiquidaciones.BuscarPorId(self.ids[1])
        self.assertIsNotNone(buscado)
        self.assertEqual(buscado.salario_base, 1600000)

    def test_buscar_liquidacion_3(self):
        buscado = ControladorLiquidaciones.BuscarPorId(self.ids[2])
        self.assertIsNotNone(buscado)
        self.assertEqual(buscado.total_liquidacion, 3925000)

    # -------------------- Pruebas de Modificación --------------------
    def test_modificar_liquidacion_1(self):
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("UPDATE liquidaciones SET prima = %s WHERE id = %s", (999999, self.ids[0]))
        cursor.connection.commit()
        buscado = ControladorLiquidaciones.BuscarPorId(self.ids[0])
        self.assertEqual(buscado.prima, 999999)

    def test_modificar_liquidacion_2(self):
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("UPDATE liquidaciones SET cesantias = %s WHERE id = %s", (888888, self.ids[1]))
        cursor.connection.commit()
        buscado = ControladorLiquidaciones.BuscarPorId(self.ids[1])
        self.assertEqual(buscado.cesantias, 888888)

    def test_modificar_liquidacion_3(self):
        cursor = ControladorLiquidaciones.ObtenerCursor()
        cursor.execute("UPDATE liquidaciones SET dias_vacaciones_pend = %s WHERE id = %s", (99, self.ids[2]))
        cursor.connection.commit()
        buscado = ControladorLiquidaciones.BuscarPorId(self.ids[2])
        self.assertEqual(buscado.dias_vacaciones_pend, 99)


if __name__ == '__main__':
    unittest.main()
