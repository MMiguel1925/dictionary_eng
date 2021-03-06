import justpy as jp
import definition
from webapp import layout
from webapp import page
import requests


class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container)
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word as you type:", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        input_box = jp.Input(a=input_div, outputdiv=output_div, placeholder="Type in a word here...",
                             classes="m-2 "
                               "bg-grey-100 "
                               "border-2 "
                               "border-gray-200 "
                               "rounded "
                               "w-64 "
                               "focus:outline-none "
                               "focus:border-purple-500 "
                               "focus:bg-white "
                               "py-2 "
                               "px-4")

        input_box.on('input', cls.get_definition)
        jp.Button(a=input_div, text="Get Definition", classes="border-2 text-gray-500",
                        click=cls.get_definition,
                        outputdiv=output_div,
                        inputbox=input_box)

        return wp

    # Definimos como staticmethod, que é um método dentro da classe que se comporta como uma função. Esta funçao nao
    # espera instancias como parametro, é independente da classe. Encontra se dentro da classe apenas por uma questao
    # de organização.
    @staticmethod
    def get_definition(widget, msg):
        # obtemos a informaçao via API, contudo temos que ter o programa da API a correr na porta 8001
        req = requests.get(f'http://localhost:8001/api?w={widget.value}')
        dados = req.json()
        widget.outputdiv.text = " ".join(dados["definition"])
        # ou obtemos directamente via a Class Definition
        # defined = definition.Definition(widget.value).get()
        # widget.outputdiv.text = " ".join(defined)
