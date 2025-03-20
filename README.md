# Calculadora-de-liquidacion

## ¿Quien hizo esto?
Valentina Mesa y Alejandra Escobar.

## ¿Que es y para que es?
Una calculadora de liquidación definitiva es una herramienta utilizada para calcular el monto final que una persona o empresa debe recibir o pagar al finalizar una relación laboral o un contrato. Se usa para determinar indemnizaciones, prestaciones sociales, vacaciones no gozadas, entre otros conceptos, garantizando que el cálculo se haga de acuerdo con las leyes laborales vigentes.

## ¿Como lo hago funcionar?
primero se necesita tener el codigo abierto y posteriormente poner ejecutar la consola, la cual es la que hace que toda la implementacion de la calculadora funcione; no se necesita otro pre-requisito solo que el usuario sea consiente y realice una buena lectura de los valores a ingresar.

## ¿Como esta hecho?
este programa contiene varias carpetas entre estas las mas esenciales para el codigo, las cuales son "model" que contiene la logica del programa, "tests" que contiene todos los casos de prueba, y finalmente "ui" que contiene la consola y es donde se debe correr para ejecutar el programa.

Entradas: para realizar una calculadora de liquidacion definitiva necesitamos principalmente 2 valores de entrada brindadas por el usuario: SALARIO Y DIAS TRABAJADOS

Proceso: continuamos con el calculo de las variables que darian el total de la liquidacion, las cuales son LA PRIMA, LAS CESANTIAS, LAS VACACIONES, LOS INTERESES DE LAS CESANTIAS (La indemnizacion si aplica) todo esto 
para llegar a unos resultados que se sumaran al final del proceso.

Salida: la unica variable de salida es el TOTAL DE LA LIQUIDACION, la cual seria el valor total que la empresa tendria que pagarle al usuario por sus servicios dentro de la empresa.

## Estructura
src: codigo fuente de la logica de la aplicacion
 * carpeta model: es la capa de la logica de negocio donde se encuentra el init.py y la logica
 * carpeta ui: es la capa de la interfaz (consola o GUI) que contiene init.py y la respectiva consola
test: pruebas unitarias
 * init.py
 * test

instalacion y requisitos: 
* asegurate de tener python 3.8 o superior intalado en el sistema
* clona el repositorio o descarga los archivos
* el proyecto no cuenta con dependencias

## Uso
para ejecutar el programa desde la consola: ui/console.py

ejecucion pruebas unitarias: 
para ejecutar las pruebas unitarias, desde la carpeta raiz se utiliza el comando: python -m unittest tests.test_logic o simplemente ve al simbolo de pruebas en visual y dale a correr para asegurarte de que todas las pruebas funcionen correctamente.



