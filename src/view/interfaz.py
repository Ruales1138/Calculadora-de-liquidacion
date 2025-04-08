from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from kivy.resources import resource_add_path
import sys
sys.path.append("src")
from model.PaymentLogic import PaymentLogic_Calculator

resource_add_path('fonts')



class ResultadosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40)
        self.resultados_label = Label(
            text="", halign='left', valign='top', font_size=16,
            color=get_color_from_hex('#FFFFFF')
        )
        layout.add_widget(self.resultados_label)
        self.add_widget(layout)
        Window.clearcolor = get_color_from_hex('#1E1E2F')

    def mostrar_resultados(self, resultados_text):
        self.resultados_label.text = resultados_text


class PaymentLogic(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.ingreso_screen = Screen(name="ingreso")
        main_layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        Window.clearcolor = get_color_from_hex('#1E1E2F')

        # Cabecera
        header = Label(
            text=" Calculadora de Liquidación ",
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=60,
            color=get_color_from_hex('#FFFFFF')
        )
        main_layout.add_widget(header)

        # Scroll
        scroll = ScrollView()
        self.ingreso_layout = GridLayout(cols=1, spacing=15, size_hint_y=None)
        self.ingreso_layout.bind(minimum_height=self.ingreso_layout.setter('height'))
        scroll.add_widget(self.ingreso_layout)

        main_layout.add_widget(scroll)
        self.ingreso_screen.add_widget(main_layout)

        def agregar_campo(texto_label, hint):
            self.ingreso_layout.add_widget(Label(
                text=texto_label,
                font_size=16,
                size_hint_y=None,
                height=30,
                color=get_color_from_hex('#FFFFFF')
            ))
            input_box = TextInput(
                hint_text=hint,
                multiline=False,
                size_hint_y=None,
                height=40,
                background_color=get_color_from_hex('#FFFFFF'),
                foreground_color=(0, 0, 0, 1),
                padding_y=[10, 10]
            )
            self.ingreso_layout.add_widget(input_box)
            return input_box

        self.Salario_input = agregar_campo("Ingrese su salario base:", "Ej: 1500000")
        self.aux_transporte_input = agregar_campo("Ingrese el auxilio de transporte:", "Ej: 140606")
        self.fecha_inicio_contrato_input = agregar_campo("Fecha inicio del contrato (dd/mm/yyyy):", "Ej: 01/01/2023")
        self.fecha_finalizacion_contrato_input = agregar_campo("Fecha finalización del contrato (dd/mm/yyyy):", "Ej: 31/12/2023")
        self.dias_vacaciones_no_gozadas_input = agregar_campo("Días de vacaciones no gozadas:", "Ej: 5")
        self.dias_primas_input = agregar_campo("Días de primas:", "Ej: 180")
        self.dias_cesantias_input = agregar_campo("Días de cesantías:", "Ej: 180")

    

        self.calcular_button = Button(
            text="Calcular Liquidación",
            size_hint_y=None,
            height=50,
            background_color=get_color_from_hex('#00C853'),
            color=get_color_from_hex('#FFFFFF'),
            font_size=16,
            bold=True
        )
        self.calcular_button.bind(on_press=self.calcular)
        self.ingreso_layout.add_widget(self.calcular_button)

        self.screen_manager.add_widget(self.ingreso_screen)

        self.resultados_screen = ResultadosScreen(name="resultados")
        self.screen_manager.add_widget(self.resultados_screen)

        return self.screen_manager

    def calcular(self, instance):
        try:
            campos = [
                self.Salario_input.text,
                self.aux_transporte_input.text,
                self.fecha_inicio_contrato_input.text,
                self.fecha_finalizacion_contrato_input.text,
                self.dias_vacaciones_no_gozadas_input.text,
                self.dias_primas_input.text,
                self.dias_cesantias_input.text
            ]
            if '' in campos:
                self.resultados_screen.mostrar_resultados(" Error: Por favor completa todos los campos.")
                self.screen_manager.current = "resultados"
                return

            salario = float(self.Salario_input.text)
            auxilio = float(self.aux_transporte_input.text)
            fecha_inicio = self.fecha_inicio_contrato_input.text
            fecha_finalizacion = self.fecha_finalizacion_contrato_input.text
            dias_vacaciones_no_gozadas = int(self.dias_vacaciones_no_gozadas_input.text)
            dias_prima = int(self.dias_primas_input.text)
            dias_cesantias = int(self.dias_cesantias_input.text)

            calculadora = PaymentLogic_Calculator(
                salario_base=salario,
                aux_transporte=auxilio,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_finalizacion,
                dias_vacaciones_pend=dias_vacaciones_no_gozadas,
                dias_prima=dias_prima,
                dias_cesantias=dias_cesantias
            )

            resultado_text = (
                f" Días Trabajados: {calculadora.dias_trabajados}\n"
                f" Años de servicio: {calculadora.calcular_anos_servicio():,.2f}\n"
                f" Indemnización: ${calculadora.calcular_indemnizacion():,.2f}\n"
                f" Vacaciones: ${calculadora.calcular_vacaciones():,.2f}\n"
                f" Cesantías: ${calculadora.calcular_cesantias():,.2f}\n"
                f" Intereses Cesantías: ${calculadora.calcular_intereses_cesantias():,.2f}\n"
                f" Prima: ${calculadora.calcular_prima():,.2f}\n"
                f" Aguinaldo: ${calculadora.calcular_aguinaldo():,.2f}\n"
                f" Total Liquidación: ${calculadora.calcular_total_liquidacion():,.2f}"
            )

            self.resultados_screen.mostrar_resultados(resultado_text)
            self.screen_manager.current = "resultados"


        except Exception as e:
            print("Error durante el cálculo:", e)


if __name__ == "__main__":
    PaymentLogic().run()
