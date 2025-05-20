# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo 
from flask import Flask    

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template, request

import sys
sys.path.append( "src" )

#from controller.tarjetas_controller import TarjetasController

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
@app.route('/')      
def index():
    return render_template("index.html")

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/lista')
def lista_tarjetas():
    #tarjetas = TarjetasController.BuscarPorCedula( request.args["cedula"]  )
    tarjetas = 'gfasgf'
    return render_template('lista.html', id=request.args["id"], tarjetas=tarjetas  )

# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True)