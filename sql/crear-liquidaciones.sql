drop table liquidaciones;
CREATE TABLE liquidaciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    empleado_id INT,
    fecha_salida DATE,
    fecha_calculo DATE,
    dias_trabajados INT,
    total_liquidacion DECIMAL(12,2),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)
);