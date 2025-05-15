# Calculadora-de-liquidacion

## ¿Quien hizo esto?
Valentina Mesa y Alejandra Escobar.

## Entrega 5
Heiver David Ruales Luna


Sara Rojas Martínez

## ¿Que es y para que es?
Una calculadora de liquidación definitiva es una herramienta utilizada para calcular el monto final que una persona o empresa debe recibir o pagar al finalizar una relación laboral o un contrato. Se usa para determinar indemnizaciones, prestaciones sociales, vacaciones no gozadas, entre otros conceptos, garantizando que el cálculo se haga de acuerdo con las leyes laborales vigentes.

## ¿Como lo hago funcionar?
Se necesita tener el codigo abierto y posteriormente poner ejecutar la consola, la cual es la que hace que toda la implementacion de la calculadora funcione; no se necesita otro pre-requisito solo que el usuario sea consiente y realice una buena lectura de los valores a ingresar.

## ✅ Funcionalidades

- Cálculo de:
  - Días trabajados y años de servicio
  - Indemnización
  - Vacaciones no gozadas
  - Cesantías e intereses sobre cesantías
  - Prima
  - Aguinaldo
  - Total de la liquidación
- Interfaz amigable y responsiva con Kivy
- Registro automático de cada liquidación en PostgreSQL
- Arquitectura estructurada por capas (MVC)
- Pruebas unitarias con `unittest`

## ¿Como esta hecho?
este programa contiene varias carpetas entre estas las mas esenciales para el codigo, las cuales son "model" que contiene la logica del programa, "tests" que contiene todos los casos de prueba, y finalmente "ui" que contiene la consola y es donde se debe correr para ejecutar el programa.

Este proyecto es una aplicación de escritorio con interfaz gráfica, diseñada para calcular la liquidación laboral de un trabajador colombiano a partir de los parámetros de su contrato. Está estructurado bajo una arquitectura modular basada en MVC (Modelo–Vista–Controlador), con integración directa a una base de datos PostgreSQL para almacenamiento persistente de cada cálculo realizado.

### Entradas: 
 para realizar una calculadora de liquidacion definitiva necesitamos principalmente 2 valores de entrada brindadas por el usuario: SALARIO Y DIAS TRABAJADOS

### Proceso: 
 continuamos con el calculo de las variables que darian el total de la liquidacion, las cuales son LA PRIMA, LAS CESANTIAS, LAS VACACIONES, LOS INTERESES DE LAS CESANTIAS (La indemnizacion si aplica) todo esto 
para llegar a unos resultados que se sumaran al final del proceso.

### Salida: 
 la unica variable de salida es el TOTAL DE LA LIQUIDACION, la cual seria el valor total que la empresa tendria que pagarle al usuario por sus servicios dentro de la empresa.

## 📂 Estructura del Proyecto

* CALCULADORA-DE-LIQUIDACION/
* ├── SQL/
* │ └── crear-liquidaciones.sql
* ├── src/
* │ ├── controller/
* │ │ └── liquidacion_controller.py
* │ ├── model/
* │ │ └── PaymentLogic.py
* │ ├── model2/
* │ │ └── liquidacion.py
* │ └── view/
* │ └── interfaz.py
* ├── tests/
* │ └── test_liquidacion.py
* ├── SecretConfig.py
* ├── README.md
* ├── .gitignore

## Cómo ejecutar la aplicación

### 1. Clona el repositorio
git clone https://github.com/usuario/Calculadora-de-liquidacion.git
cd Calculadora-de-liquidacion

### 2. Instala las dependencias
pip install kivy psycopg2

### 3. Configura la base de datos
edita el archivo SecretConfig-sample en la raiz del proyecto

* PGHOST='PONGA EL HOST DE LA BD AQUI'
* PGDATABASE='PONGA EL NOMBRE DE LA BD AQUI'
* PGUSER='PONGA EL USUARIO AQUI'
* PGPASSWORD='PONGA LA CONTRASEÑA AQUI'
* PGPORT="5432"

### 4. crea la tabla
psql -U tu_usuario -d nombre_de_tu_bd -f SQL/crear-liquidaciones.sql

### 5. ejecuta la aplicación
python src/view/interfaz.py

## Ejecutar las pruebas unitarias

* python -m unittest discover -s tests

## Tecnologías usadas

* Python 3.8+
* Kivy (interfaz gráfica)
* PostgreSQL (almacenamiento de resultados)
* psycopg2 (driver PostgreSQL)
* unittest (pruebas)

## Uso
para ejecutar el programa desde la consola: ui/console.py




