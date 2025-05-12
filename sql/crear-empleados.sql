drop table empleados;
CREATE TABLE empleados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    cedula VARCHAR(20) UNIQUE,
    fecha_ingreso DATE,
    salario DECIMAL(10,2),
    cargo VARCHAR(100)
);
