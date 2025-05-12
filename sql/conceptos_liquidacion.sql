drop table conceptos_liquidaciones;
CREATE TABLE conceptos_liquidacion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    liquidacion_id INT,
    concepto VARCHAR(100),  -- Ej: "Vacaciones no gozadas", "Aguinaldo"
    monto DECIMAL(10,2),
    FOREIGN KEY (liquidacion_id) REFERENCES liquidaciones(id)
);