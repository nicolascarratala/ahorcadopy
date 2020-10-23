
class Ahorcado ():

    def request_letter(self):
        text = "Escriba letra porfavor"
        return input(text)

    def un_jugador(self):

        self.adivinanza = ['P', 'A', 'L', 'A', 'B', 'R', 'A', '1', '2', '3']

        # INPUT NOMBRE
        self.name = str(input('Elija un nombre '))

        # INPUT DIFICULTAD
        self.dificultad = int(input(
                'Elija dificultad(del uno al 10, el 1 es mas dificil)'))

        self.coinciden = 0
        self.diferentes = 0

        self.vidas = len(self.adivinanza)*self.dificultad

        self.listLetters = []

        self.history = []

        self.flag = True

        while(self.flag):

            self.letter = Ahorcado().request_letter()
            print(self.letter)
            self.present = False

            # Salir del juego
            if self.letter == "salir":
                self.flag = False
                print('Saliste del juego')
                return True

            if self.flag is True:

                # Reconocer letras usadas
                for used in self.history:
                    if self.letter == used:
                        self.present = True
                
                if self.present is not True:
                    for x in range(len(self.adivinanza)):
                        if self.letter == self.adivinanza[x]:
                            self.coinciden += 1
                            self.listLetters.append(self.adivinanza[x])
                            self.history.append(self.adivinanza[x])
                        if self.letter != self.adivinanza[x]:
                            self.diferentes += 1
                    if self.coinciden > 0:
                        print("Correcta")
                    if self.coinciden == 0 and self.diferentes > 0:
                        print("Fallo")
                        self.vidas -= 1
                    self.coinciden = 0
                    self.diferentes = 0
                    for x in self.listLetters:
                        self.adivinanza.remove(x)
                    del self.listLetters[:]
                    if self.vidas == 0:
                        self.flag = False
                        print('Perdiste')
                        return False
                    if len(self.adivinanza) == 0 and self.vidas > 0:
                        self.flag = False
                        print('Ganaste')
                        return True

                if self.present is True:
                    print("Letra anteriormente usada")

    def dos_jugadores(self):

        self.resultadoA = False
        self.resultadoB = False

        for juegos in range(2):

            print("Juego: "+str(juegos))

            self.adivinanza = []
            self.name = ""
            self.dificultad = ""
            self.palabra_adivinar = ""
            self.tipo_palabra_adivinar = ""
            self.coinciden = 0
            self.diferentes = 0
            self.listLetters = []
            self.history = []
            self.flag = True
            self.vidas = 0

            # INPUT NOMBRE
            self.name = str(input('Elija un nombre '))

            # INPUT DIFICULTAD
            self.dificultad = int(input(
                    'Elija dificultad(1=Facil,2=Medio,3=Dificil): '))

            # INPUT PALABRA A ADIVINAR
            self.palabra_adivinar = str(input(
                '¿Palabra que va a adivinar?')).upper()

            for j in self.palabra_adivinar:
                self.adivinanza.append(j)

            print(self.adivinanza)

            # INPUT TIPO DE PALABRA
            self.tipo_palabra_adivinar = str(input('¿Tipo de palabra?'))

            if self.dificultad == 1:
                self.vidas = 5
            if self.dificultad == 2:
                self.vidas = 3
            if self.dificultad == 3:
                self.vidas = 1

            while(self.flag):
                self.letter = Ahorcado().request_letter()
                print(self.letter)
                self.present = False

                if self.letter == "salir":
                    self.flag = False
                    print('Saliste del juego')
                    return True

                if self.flag is True:
                    for used in self.history:
                        if self.letter == used:
                            self.present = True

                    if self.present is not True:
                        for x in range(len(self.adivinanza)):
                            if self.letter == self.adivinanza[x]:
                                self.coinciden += 1
                                self.listLetters.append(self.adivinanza[x])
                                self.history.append(self.adivinanza[x])
                            if self.letter != self.adivinanza[x]:
                                self.diferentes += 1
                        if self.coinciden > 0:
                            print("Correcta")
                        if self.coinciden == 0 and self.diferentes > 0:
                            print("Fallo")
                            self.vidas -= 1
                        self.coinciden = 0
                        self.diferentes = 0
                        for x in self.listLetters:
                            self.adivinanza.remove(x)
                        del self.listLetters[:]
                        if self.vidas == 0:
                            self.flag = False
                            print('Perdiste')
                            if juegos == 0:
                                self.resultadoA = False
                            if juegos == 1:
                                self.resultadoB = False
                        if len(self.adivinanza) == 0 and self.vidas > 0:
                            self.flag = False
                            print('Ganaste')
                            if juegos == 0:
                                self.resultadoA = True
                            if juegos == 1:
                                self.resultadoB = True

                    if self.present is True:
                        print("Letra anteriormente usada")

        print("Jugador 1 : " + str(self.resultadoA))
        print("Jugador 2 : " + str(self.resultadoB))

        return self.resultadoA
