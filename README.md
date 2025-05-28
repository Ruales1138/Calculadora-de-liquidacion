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
* ├── sql/
* │ └── crear-conceptos_liquidacion.sql
* │ └── crear-empleados.sql
* │ └── crear-historial_salarios.sql
* │ └── crear-liquidaciones.sql
* ├── src/
* ├── console/
*  │ └── console.py
* │ ├── controller/
* │ │ └── conceptos_liquidaciones_controller.py
* │ │ └── empleados_controller.py
* │ │ └── historial_salarios_controller.py
* │ │ └── liquidaciones_controller.py
* │ ├── model/
* │ │ └── PaymentLogic.py
* │ │ └── __init__.py
* │ ├── model2/
* │ │ └── conceptos_liquidaciones.py
* │ │ └── empleados.py
* │ │ └── historial_salarios.py
* │ │ └── liquidacion.py
* │ │ └── liquidaciones.py
* │ ├── view/
* │ │ └── interfaz.py
* │ │ ├── web/
* │ │ │ └── vista_liquidacion.py
* │ ├── templates/
* │ │ └── buscar.html
* │ │ └── confirmacion.html
* │ │ └── crear.html
* │ │ └── index.html
* │ │ └── insertar.html
* │ │ └── lista.html
* │ │ └── modificar.html
* ├── tests/
* │ └── __init__.py
* │ └── test_PaymentLogic.py
* │ └── test_empleadosdb.py
* ├── .gitignore
* ├── Casos_de_prueba.xlsx
* ├── README.md
* ├── SecretConfig-sample.py
* ├── app.py
* ├── requirements.txt

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

## Entregable de página web

** ¿Cómo ejecutar la aplicación web?

Para comenzar a utilizar la aplicación web, debes de instalar la libreria de Flask, con el siguiente comando:

```
pip install Flask
```

Luego ejecuta el siguiente comando desde la terminal:

```
python3 -m flask run --debug
```

**¿Cómo ejecutarlo desde Render.com?**

Primero, tienes que ingresar a Render.com y crea una cuenta, luego haz click en el botón páginas web y ahi puedes crear un proyecto nuevo, luego ingresa los siguientes parámetros donde te los pida en la configuración del proyecto:

En el build command, ingresa:
```
pip install -r requirements.txt
```
En Start Command ingresa:
```
flask run -p 10000 -h 0.0.0.0

```
Y cuando te pida url del proyecto ingresa el link de este proyecto de Github.

Una vez hechos los pasos anteriores, inicializa la página y espera que se construya, una vez hecho eso, abre el link en una pestaña nueva y listo

**Link del Render**

https://calculadora-de-liquidacion-u1j7.onrender.com


## Tecnologías usadas

* Python 3.8+
* Kivy (interfaz gráfica)
* PostgreSQL (almacenamiento de resultados)
* psycopg2 (driver PostgreSQL)
* unittest (pruebas)

## Uso
para ejecutar el programa desde la consola: ui/console.py




