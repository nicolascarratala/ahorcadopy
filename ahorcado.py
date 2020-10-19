
class Ahorcado():

    def un_jugador(self):
        nombre = input('Elija un nombre: ')
        adivinanza = ['P', 'A', 'L', 'A', 'B', 'R', 'A', '1', '2', '3']
        dificultad = int(input(
            'Elija dificultad(1=dificil,2=medio,3=facil): '))
        pos = 0
        bandera = True
        bien = 0

        print('Hola '+nombre)

        while(bandera):
            letra = str(input('Escriba letra: ')).upper()
            print('Letra elegida: '+letra)

            for a in adivinanza:
                if a == letra:
                    adivinanza.pop(pos)
                    print('Bien!!!, faltan '+str(len(adivinanza))+' letras')
                    bien += 1
                    break
                if a != letra:
                    dificultad -= 1
                    print('Mal, te quedan '+str(dificultad)+' intentos')
                    # sumar parte cuerpo v2
                    break
                pos += 1

            if dificultad == 0:
                print('Perdiste alpiste')
                bandera = False
                return False
            if bien == 10:
                print('Ganaste, buen trabajo')
                bandera = False
                return True

Ahorcado().un_jugador()
