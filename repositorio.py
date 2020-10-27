import random


class Repositorio:
    def __init__(self):
        pass

    def falta_palabra(self):
        palabras = ['astros', 'emojis', 'clavos', 'bonita', 'Albaca']
        tipos = ['Astronomía', 'Chat', 'Herramientas', 'Cumplido', 'Planta']

        indice = random.randrange(0, 4)

        return {'palabra': palabras[indice], 'tipo_palabra': tipos[indice]}
