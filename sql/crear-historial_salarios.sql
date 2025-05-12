drop table historial_salarios;
CREATE TABLE historial_salarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    empleado_id INT,
    salario DECIMAL(10,2),
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)
);