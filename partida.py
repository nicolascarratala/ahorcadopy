class Partida:
    def __init__(self, palabra, intentos, tipo_palabra, nombre_jugador):
        self._palabra = palabra
        self._intentos = intentos
        self._tipo_palabra = tipo_palabra
        self._nombre_jugador = nombre_jugador
        self._palabra_aciertos = [None, None, None, None, None, None]
        Partida.campos_erroneos(self)
        Partida.mayusculas(self)
        Partida.ordenar_palabra(self)


    # palabra
    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, val):
        self._palabra = val

    # intetnos
    @property
    def intentos(self):
        return self._intentos

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, val):
        self._palabra_aciertos = val

    def ordenar_palabra(self):
        lista = []
        for j in self._palabra:
            lista.append(j)
        self._palabra = lista

    def mayusculas(self):
        self._palabra = self._palabra.upper()
        self._tipo_palabra = self._tipo_palabra.upper()
        self._nombre_jugador = self._nombre_jugador.upper()

    def campos_erroneos(self):
        if self._palabra == '':
            raise ValueError
        if self._nombre_jugador == '':
            raise ValueError
        if self._tipo_palabra == '':
            raise ValueError
        if self._intentos < 0:
            raise ValueError

    def reiniciar_aciertos(self):
        self.palabra_aciertos = []
        for k in self._palabra:
            self.palabra_aciertos.append(None)

