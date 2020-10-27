from ahorcado import Ahorcado
from ui import Ui


class Menu:
    def menu(self):

        while True:

            print('BIENVENIDO A AHORCADO PY')

            print('Elija una opción:')

            print('1: Un jugador')

            print('2: Dos jugador')

            try:
                opcion = int(input('>'))
            except ValueError as e:
                print("No se aceptan letras, Elija otra opción")

            if  opcion > 0 and opcion < 3:

                if opcion == 1:
                    print('Juega uno')
                    Ahorcado.un_jugador_nuevo(self)

                if opcion == 2:
                    print('Juegan dos')
                    Ahorcado.dos_jugadores_nuevos(self)


if __name__ == '__main__':
    a = Menu()
    a.menu()