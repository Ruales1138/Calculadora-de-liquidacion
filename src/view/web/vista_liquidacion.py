from flask import Blueprint, render_template, request

blueprint = Blueprint( "vista_liquidacion", __name__, "templates" )

import sys
sys.path.append("src")
from controller.liquidaciones_controller import ControladorLiquidaciones


@blueprint.route("/")
def Home():
   return render_template("index.html")

@blueprint.route('/buscar')
def buscar():
    return render_template('buscar.html')

@blueprint.route('/lista')
def lista_liquidacion():
    buscado = ControladorLiquidaciones.BuscarPorId(request.args["id"])
    return render_template('lista.html', id=request.args["id"], buscado=buscado  )