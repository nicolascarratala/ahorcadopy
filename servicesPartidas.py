from partida import Partida
from repositorio import Repositorio
from ui import Ui


class ServicesPartidas:

    def __init__(self):
        pass

    def iniciar_partida(self, nombre, intentos, palabra, tipo):
        if palabra == '':
            nuevas = ServicesPartidas.get_random_palabra(self)
            palabra = nuevas['palabra']
            tipo = nuevas['tipo_palabra']
        if intentos < 1 or intentos > 10:
            raise ValueError
        a = (len(palabra) * intentos)
        return Partida(palabra, a, tipo, nombre)

    def intentar_letra(self, partida, letra):

        print('Turno jugador 1: ' + partida._nombre_jugador)

        for x in range(len(partida.palabra)):
            if partida._intentos == 0:
                raise ValueError
            if letra == partida.palabra[x]:
                print('Bien!')
                partida.palabra_aciertos[x] = partida.palabra[x]
            if partida.palabra == partida.palabra_aciertos:
                StrA = "".join(partida._palabra)
                print(StrA)
                return 'Gano'

        partida._intentos -= 1

        Ui.salto(self)

        print('Intentos: ' + str(partida._intentos))

        print('Tipo de palabra: ' +  partida._tipo_palabra )

        print('Letra adivindadas : ' + str(partida._palabra_aciertos))


        if partida._intentos == 0:
            return 'Perdio'
        if partida._intentos > 0 and partida.palabra_aciertos != partida.palabra:
            return 'Continua'

    def get_random_palabra(self):
        return Repositorio.falta_palabra(self)

