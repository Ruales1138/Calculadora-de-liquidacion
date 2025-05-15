CREATE TABLE liquidaciones (
    id SERIAL PRIMARY KEY,
    nombre_empleado VARCHAR(100) NOT NULL,
    cedula_empleado VARCHAR(20) NOT NULL,
    fecha_ingreso DATE NOT NULL,
    fecha_salida DATE NOT NULL,
    salario_base NUMERIC(15, 2) NOT NULL,
    dias_laborados INT NOT NULL,
    total_liquidacion NUMERIC(15, 2) NOT NULL,
    fecha_calculo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 