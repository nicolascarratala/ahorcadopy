from partida import Partida
from servicesPartidas import ServicesPartidas
from ui import Ui


class Ahorcado:
  def request_letter(self):
    text = "Escriba letra porfavor"
    return input(text)

  def un_jugador(self):

    self.adivinanza = ['P', 'A', 'L', 'A', 'B', 'R', 'A', '1', '2', '3']

    # INPUT NOMBRE
    self.name = str(input())

    # INPUT DIFICULTAD
    self.dificultad = int(input())

    self.coinciden = 0
    self.diferentes = 0

    self.vidas = len(self.adivinanza)*self.dificultad

    self.listLetters = []

    self.history = []

    self.flag = True

    while(self.flag):

      self.letter = Ahorcado().request_letter()
      self.present = False

      # Salir del juego
      if self.letter == "salir":
        self.flag = False
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
          if self.coinciden == 0 and self.diferentes > 0:
            self.vidas -= 1
          self.coinciden = 0
          self.diferentes = 0
          for x in self.listLetters:
            self.adivinanza.remove(x)
          del self.listLetters[:]
          if self.vidas == 0:
            self.flag = False
            return False
          if len(self.adivinanza) == 0 and self.vidas > 0:
            self.flag = False
            return True


  def dos_jugadores(self):

    self.resultadoA = False
    self.resultadoB = False

    for juegos in range(2):

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
      self.name = str(input())

      # INPUT DIFICULTAD
      self.dificultad = int(input())

      # INPUT PALABRA A ADIVINAR
      self.palabra_adivinar = str(input()).upper()

      for j in self.palabra_adivinar:
        self.adivinanza.append(j)


      # INPUT TIPO DE PALABRA
      self.tipo_palabra_adivinar = str(input())

      if self.dificultad == 1:
        self.vidas = 5
      if self.dificultad == 2:
        self.vidas = 3
      if self.dificultad == 3:
        self.vidas = 1

      while(self.flag):
        self.letter = Ahorcado().request_letter()

        self.present = False

        if self.letter == "salir":
          self.flag = False

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

            if self.coinciden == 0 and self.diferentes > 0:
              self.vidas -= 1
            self.coinciden = 0
            self.diferentes = 0
            for x in self.listLetters:
              self.adivinanza.remove(x)
            del self.listLetters[:]
            if self.vidas == 0:
              self.flag = False
              if juegos == 0:
                self.resultadoA = False
              if juegos == 1:
                self.resultadoB = False
            if len(self.adivinanza) == 0 and self.vidas > 0:
              self.flag = False
              if juegos == 0:
                self.resultadoA = True
              if juegos == 1:
                self.resultadoB = True



    return self.resultadoA

  def un_jugador_nuevo(self):

    print('Escribe tu nombre:')

    nombre = str(input('>'))

    print('Elija dificultad del 1 al 10')

    dificultad = int(input(">"))

    partida = ServicesPartidas.iniciar_partida(self, nombre, dificultad, '', '')

    bandera = True

    while(bandera):

      try:

        print('Ingrese una letra ')

        letra = str(input('>')).upper()

        juego = ServicesPartidas.intentar_letra(self, partida, letra)

        if juego == 'Gano':
          print('')
          print('la palabra era:' + str(partida._palabra_aciertos))
          Ui.linea(self)
          print('Ganaste!!! 🔥💐🎊🎉')

          bandera = False

        if juego == 'Perdio':
          print('Perdiste 😭')
          bandera = False


      except ValueError:

        print('Se te terminaron las chafis')

        bandera = False

    print('Game Games Games')
    Ui.linea(self)
    print('')
    Ui.linea(self)

  def dos_jugadores_nuevos(self):

    jugador1 = {
      "_nombre": '',
      "_palabra": '',
      "_tipo_palabra": '',
      '_intentos':0,
      '_palabra_aciertos':[],
    }
    jugador2 = {
      "_nombre": '',
      "_palabra": '',
      "_tipo_palabra": '',
      '_intentos': 0,
      '_palabra_aciertos': [],
    }

    datos = {
      "JUGADOR1": jugador1,
      "JUGADOR2": jugador2,
    }

    print('Elija dificultad del 1 al 10')
    dificultad = int(input(">"))

    print(' Jugador 1 Ingresa el nombre del otro jugador')
    jugador1["_nombre"] = str(input('>'))
    print ('ingrese el tipo de palabra')
    jugador1["_tipo_palabra"] = str(input('>'))
    print('ingrese la palabra a adivinar')
    jugador1["_palabra"] = str(input('>'))

    jugador1["_intentos"] = dificultad

    print('')

    print('Jugador 2 ingresa el nombre del otro jugador')
    jugador2["_nombre"] = str(input('>'))
    print('ingrese el tipo de palabra')
    jugador2["_tipo_palabra"] = str(input('>'))
    print('ingrese la palabra a adivinar')
    jugador2["_palabra"] = str(input('>'))
    print('ingrese la cantidad de intentos')
    jugador2["_intentos"] = dificultad

    print('')
    print('')

    print('Tu turno jugador ' + jugador1['_nombre'].upper())

    partida1 = ServicesPartidas.iniciar_partida(self, jugador1['_nombre'], dificultad, jugador1['_palabra'], jugador1['_tipo_palabra'])

    partida1.reiniciar_aciertos()

    bandera1 = True

    while(bandera1):

      try:

        print('Ingrese una letra ')

        letra = str(input('>')).upper()

        juego = ServicesPartidas.intentar_letra(self, partida1, letra)


        if juego == 'Gano':
          print('')
          jugador1['_palabra_aciertos'] = partida1.palabra_aciertos
          print('la palabra era:' + str(partida1._palabra_aciertos))
          Ui.linea(self)
          print('Ganaste!!! 🔥💐🎊🎉')
          bandera1 = False

        if juego == 'Perdio':
          print('Perdiste 😭')
          bandera1 = False


      except ValueError:

        print('Se te terminaron las chafis')

        bandera1 = False

    print('')
    print('')
    print('Tu turno jugador '+jugador2['_nombre'].upper())


    partida2 = ServicesPartidas.iniciar_partida(self,jugador2['_nombre'], dificultad, jugador2['_palabra'], jugador2['_tipo_palabra'])

    partida2.reiniciar_aciertos()

    bandera2 = True

    while (bandera2):

      try:

        print('Ingrese una letra ')

        letra = str(input('>')).upper()

        juego = ServicesPartidas.intentar_letra(self, partida2, letra)

        if juego == 'Gano':
          print('')
          jugador2['_palabra_aciertos'] = partida2.palabra_aciertos
          print('la palabra era:' + str(partida2._palabra_aciertos))
          Ui.linea(self)
          print('Ganaste!!! 🔥💐🎊🎉')
          bandera2 = False

        if juego == 'Perdio':
          print('Perdiste 😭')
          bandera2= False


      except ValueError:

        print('Se te terminaron las chafis')

        bandera2 = False

    print(datos)

    print('Game Games Games')
    Ui.linea(self)
    print('')
    Ui.linea(self)