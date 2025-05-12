drop table conceptos_liquidacion;
CREATE TABLE conceptos_liquidacion (
    id SERIAL PRIMARY KEY,
    liquidacion_id INT,
    concepto VARCHAR(100),
    monto DECIMAL(10,2),
    FOREIGN KEY (liquidacion_id) REFERENCES liquidaciones(id)
);