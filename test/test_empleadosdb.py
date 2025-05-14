import os
import sys
sys.path.append("src")
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import unittest
from datetime import date
from src.controller.empleados_controller import ControladorEmpleado
from src.model2.empleados import Empleado

class TestControladorEmpleado(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ControladorEmpleado.EliminarTabla()
        ControladorEmpleado.CrearTabla()

    def setUp(self):
        # Limpia la tabla antes de cada prueba
        cursor = ControladorEmpleado.ObtenerCursor()
        cursor.execute("DELETE FROM empleados")
        cursor.connection.commit()

    # --------------- Pruebas de inserción ---------------

    def test_insertar_empleado_1(self):
        emp = Empleado(1, "Laura", "Gomez", "111", date(2022, 5, 1), 2500000, "Analista")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(1)
        emp.esIgual(emp_db)

    def test_insertar_empleado_2(self):
        emp = Empleado(2, "Carlos", "Perez", "222", date(2023, 1, 15), 3200000, "Ingeniero")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(2)
        emp.esIgual(emp_db)

    def test_insertar_empleado_3(self):
        emp = Empleado(3, "Sandra", "Lopez", "333", date(2021, 7, 30), 2800000, "Técnico")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(3)
        emp.esIgual(emp_db)

    # --------------- Pruebas de modificación ---------------

    def test_modificar_empleado_1(self):
        emp = Empleado(4, "Luis", "Mora", "444", date(2020, 3, 10), 3000000, "Jefe")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp.nombre = "Luis Alberto"
        ControladorEmpleado.ActualizarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(4)
        emp.esIgual(emp_db)

    def test_modificar_empleado_2(self):
        emp = Empleado(5, "Angela", "Rincon", "555", date(2019, 8, 1), 3100000, "Coordinadora")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp.salario = 3500000
        ControladorEmpleado.ActualizarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(5)
        emp.esIgual(emp_db)

    def test_modificar_empleado_3(self):
        emp = Empleado(6, "Diego", "Martinez", "666", date(2018, 12, 15), 2950000, "Auxiliar")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp.cargo = "Supervisor"
        ControladorEmpleado.ActualizarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(6)
        emp.esIgual(emp_db)

    # --------------- Pruebas de búsqueda ---------------

    def test_buscar_empleado_1(self):
        emp = Empleado(7, "Cesar", "Nuñez", "777", date(2022, 10, 5), 2700000, "Contador")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(7)
        emp.esIgual(emp_db)

    def test_buscar_empleado_2(self):
        emp = Empleado(8, "Patricia", "Salas", "888", date(2023, 3, 3), 2600000, "Consultora")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(8)
        emp.esIgual(emp_db)

    def test_buscar_empleado_3(self):
        emp = Empleado(9, "Jorge", "Rivera", "999", date(2020, 9, 9), 3100000, "Diseñador")
        ControladorEmpleado.InsertarEmpleado(emp)
        emp_db = ControladorEmpleado.BuscarEmpleadoId(9)
        emp.esIgual(emp_db)

if __name__ == '__main__':
    unittest.main()