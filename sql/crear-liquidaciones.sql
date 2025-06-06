CREATE TABLE liquidaciones (
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
