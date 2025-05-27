from flask import Blueprint, render_template, request

blueprint = Blueprint( "vista_liquidacion", __name__, "templates" )

import sys
sys.path.append("src")
from controller.liquidaciones_controller import ControladorLiquidaciones
from model.PaymentLogic import PaymentLogic_Calculator


@blueprint.route("/")
def Home():
   return render_template("index.html")

@blueprint.errorhandler(Exception)
def controlar_errores(err):
    return f'Ocurrio un error en los datos ingresados: {err}'

@blueprint.route('/buscar')
def buscar():
    return render_template('buscar.html')

@blueprint.route('/lista')
def lista_liquidacion():
    buscado = ControladorLiquidaciones.BuscarPorId(request.args["id"])
    return render_template('lista.html', id=request.args["id"], buscado=buscado  )

@blueprint.route('/insertar')
def insertar():
    return render_template('insertar.html')

@blueprint.route('/confirmacion')
def confirmacion():
    # liquidacion = PaymentLogic_Calculator(
    #     request.args['salario_base'], 
    #     request.args['aux_transporte'], 
    #     request.args['fecha_inicio'], 
    #     request.args['fecha_fin'], 
    #     request.args['dias_vacaciones_pend'], 
    #     request.args['dias_prima'], 
    #     request.args['dias_cesantias'])
    
    salario_base = 3000000
    aux_transporte = 0
    fecha_inicio = "01/06/2023"
    fecha_fin = "31/12/2023"
    dias_vacaciones_pend = 5
    dias_prima = 90
    dias_cesantias = 90
    
    liquidacion = PaymentLogic_Calculator(salario_base, aux_transporte, fecha_inicio, fecha_fin, dias_vacaciones_pend, dias_prima, dias_cesantias)
    return render_template('confirmacion.html', liquidacion=liquidacion.resumen_liquidacion())