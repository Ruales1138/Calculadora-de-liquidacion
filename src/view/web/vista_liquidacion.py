from flask import Blueprint, render_template, request

blueprint = Blueprint( "vista_liquidacion", __name__, "templates" )

import sys
sys.path.append("src")
from controller.liquidaciones_controller import ControladorLiquidaciones
from model.PaymentLogic import PaymentLogic_Calculator
from model2.liquidacion import Liquidacion
from datetime import datetime, timedelta


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
    liquidacion = PaymentLogic_Calculator(
        float(request.args['salario_base']), 
        float(request.args['aux_transporte']), 
        request.args['fecha_inicio'], 
        request.args['fecha_fin'], 
        int(request.args['dias_vacaciones_pend']), 
        int(request.args['dias_prima']), 
        int(request.args['dias_cesantias'])
    )
    base_date = datetime(2023, 1, 1)
    liquidacion_2 = Liquidacion(
                id=None,
                salario_base=float(request.args['salario_base']),
                aux_transporte=float(request.args['aux_transporte']),
                fecha_inicio=base_date,
                fecha_fin=base_date + timedelta(days=365),
                dias_trabajados=365,
                anos_servicio=1.0,
                dias_vacaciones_pend=int(request.args['dias_vacaciones_pend']),
                dias_prima=int(request.args['dias_prima']),
                dias_cesantias=int(request.args['dias_cesantias']),
                indemnizacion=1500000,
                vacaciones=250000,
                cesantias=400000,
                intereses_cesantias=48000,
                prima=400000,
                aguinaldo=125000,
                total_liquidacion=3725000,
                fecha_calculo=datetime.now()
            )
    ControladorLiquidaciones.InsertarLiquidacion(liquidacion_2)
    return render_template('confirmacion.html', liquidacion=liquidacion.resumen_liquidacion())

@blueprint.route('/crear')
def crear():
    ControladorLiquidaciones.EliminarTabla()
    ControladorLiquidaciones.CrearTabla()
    return render_template('crear.html')

@blueprint.route('/modificar')
def modificar():
    id = request.args.get('id')
    buscado = ControladorLiquidaciones.BuscarPorId(id)
    return render_template('modificar.html', buscado=buscado)

@blueprint.route('/confirmar_modificacion')
def confirmar_modificacion():
    from model2.liquidacion import Liquidacion
    from datetime import datetime

    liquidacion = Liquidacion(
        id=int(request.args['id']),
        salario_base=float(request.args['salario_base']),
        aux_transporte=float(request.args['aux_transporte']),
        fecha_inicio=datetime.strptime(request.args['fecha_inicio'], "%Y-%m-%d"),
        fecha_fin=datetime.strptime(request.args['fecha_fin'], "%Y-%m-%d"),
        dias_trabajados=(datetime.strptime(request.args['fecha_fin'], "%Y-%m-%d") - datetime.strptime(request.args['fecha_inicio'], "%Y-%m-%d")).days,
        anos_servicio=round((datetime.strptime(request.args['fecha_fin'], "%Y-%m-%d") - datetime.strptime(request.args['fecha_inicio'], "%Y-%m-%d")).days / 365, 2),
        dias_vacaciones_pend=int(request.args['dias_vacaciones_pend']),
        dias_prima=int(request.args['dias_prima']),
        dias_cesantias=int(request.args['dias_cesantias']),
        indemnizacion=float(request.args['indemnizacion']),
        vacaciones=float(request.args['vacaciones']),
        cesantias=float(request.args['cesantias']),
        intereses_cesantias=float(request.args['intereses_cesantias']),
        prima=float(request.args['prima']),
        aguinaldo=float(request.args['aguinaldo']),
        total_liquidacion=float(request.args['total_liquidacion']),
        fecha_calculo=datetime.now()
    )

    ControladorLiquidaciones.EditarLiquidacion(liquidacion)
    return f"La liquidación con ID {liquidacion.id} fue modificada exitosamente."

