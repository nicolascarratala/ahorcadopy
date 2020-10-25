import unittest
from parameterized import parameterized
from partida import Partida
#from servicesPartidas import ServicesPartidas


class TestPartida(unittest.TestCase):

    # Crea una partida con valores iniciales.
    # palabra_acierto: se guarda las letras acertadas por el usuario
    # tipo_palabra: para dar orientacion al jugador
    # palabra: palabra que tiene que adivinar
    def test_constructor_con_valores_iniciales_partida(self):
        partida = Partida('python', 2, 'lenguaje de programacion', 'Claudio')
        self.assertDictEqual(partida.__dict__, {'_palabra':
                                                    ['P', 'Y', 'T', 'H', 'O', 'N'],
                                                '_tipo_palabra':
                                                    'LENGUAJE DE PROGRAMACION',
                                                '_intentos': 2,
                                                '_nombre_jugador': 'CLAUDIO',
                                                '_palabra_aciertos':
                                                    [None, None, None, None, None,
                                                     None], })

    # Verificar exceptions, palabra no puede ser vacia
    def test_exceptions_valor_inicial_palabra(self):
        with self.assertRaises(ValueError):
            Partida('', 2, 'lenguaje de programacion', 'Claudio')

    # Verificar exceptions nombre_jugador no puede ser vacia
    def test_exceptions_valor_inicial_nombre_jugador(self):
        with self.assertRaises(ValueError):
            Partida('Python', 2, 'lenguaje de programacion', '')

    # Verificar exceptions tipo_palabra no puede ser vacia
    def test_exceptions_valor_inicial_tipo_palabra(self):
        with self.assertRaises(ValueError):
            Partida('Python', 2, '', 'Claudio')

    # Verificar exceptions intentos no puede ser negativo,
    # anularia intentos
    def test_exceptions_valor_inicial_intentos(self):
        with self.assertRaises(ValueError):
            Partida('Python', -1, 'lenguaje de programacion', 'Claudio')



if __name__ == '__main__':
    unittest.main()
