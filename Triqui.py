import sys

tableroJuego = {'up-izq': ' ', 'up-med': ' ', 'up-der': ' ',
            'mid-izq': ' ', 'mid-med': ' ', 'mid-der': ' ',
            'down-izq': ' ', 'down-med': ' ', 'down-der': ' '}


def validarX(tableroJuego):
    if ((tableroJuego['up-izq']=='X' and tableroJuego['up-med']=='X' and tableroJuego['up-der']=='X') or
        (tableroJuego['mid-izq']=='X' and tableroJuego['mid-med']=='X' and tableroJuego['mid-der']=='X') or
        (tableroJuego['down-izq']=='X' and tableroJuego['down-med']=='X' and tableroJuego['down-der']=='X') or
        (tableroJuego['up-izq']=='X' and tableroJuego['mid-izq']=='X' and tableroJuego['down-izq']=='X') or
        (tableroJuego['up-med']=='X' and tableroJuego['mid-med']=='X' and tableroJuego['down-med']=='X') or
        (tableroJuego['up-der']=='X' and tableroJuego['mid-der']=='X' and tableroJuego['down-der']=='X') or
        (tableroJuego['up-izq']=='X' and tableroJuego['mid-med']=='X' and tableroJuego['down-der']=='X') or
        (tableroJuego['down-izq']=='X' and tableroJuego['mid-med']=='X' and tableroJuego['up-der']=='X')):
        return True
    return False

def validarO(tableroJuego):
    if ((tableroJuego['up-izq']=='O' and tableroJuego['up-med']=='O' and tableroJuego['up-der']=='O') or
        (tableroJuego['mid-izq']=='O' and tableroJuego['mid-med']=='O' and tableroJuego['mid-der']=='O') or
        (tableroJuego['down-izq']=='O' and tableroJuego['down-med']=='O' and tableroJuego['down-der']=='O') or
        (tableroJuego['up-izq']=='O' and tableroJuego['mid-izq']=='O' and tableroJuego['down-izq']=='O') or
        (tableroJuego['up-med']=='O' and tableroJuego['mid-med']=='O' and tableroJuego['down-med']=='O') or
        (tableroJuego['up-der']=='O' and tableroJuego['mid-der']=='O' and tableroJuego['doown-der']=='O') or
        (tableroJuego['up-izq']=='O' and tableroJuego['mid-med']=='O' and tableroJuego['down-der']=='O') or
        (tableroJuego['down-izq']=='O' and tableroJuego['mid-med']=='O' and tableroJuego['up-der']=='O')):
        return True
    return False


def esGanadorO(band):
    if band==True:
        print("El ganador es el jugador 2")
        sys.exit()
    

def esGanadorX(band):
    if band==True:
        print("El ganador es el jugador 1")
        sys.exit()
    
    
    
def imprimirTablero(tablero):
    print(tableroJuego['up-izq'] + '|' + tableroJuego['up-med'] + '|' + tableroJuego['up-der'])
    print('-+-+-')
    print(tableroJuego['mid-izq'] + '|' + tableroJuego['mid-med'] + '|' + tableroJuego['mid-der'])
    print('-+-+-')
    print(tableroJuego['down-izq'] + '|' + tableroJuego['down-med'] + '|' + tableroJuego['down-der'])

print("Bienvenido al juego Triqui!!!")
imprimirTablero(tableroJuego)

def jugadorUno(posicion, tableroJuego):
    if(posicion == 'up-izq'):
        if(tableroJuego['up-izq'] == ' '):
            tableroJuego['up-izq'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'up-med'):
        if(tableroJuego['up-med'] == ' '):
            tableroJuego['up-med'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'up-der'):
        if(tableroJuego['up-der'] == ' '):
            tableroJuego['up-der'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'mid-izq'):
        if(tableroJuego['mid-izq'] == ' '):
            tableroJuego['mid-izq'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'mid-med'):
        if(tableroJuego['mid-med'] == ' '):
            tableroJuego['mid-med'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'mid-der'):
        if(tableroJuego['mid-der'] == ' '):
            tableroJuego['mid-der'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'down-izq'):
        if(tableroJuego['down-izq'] == ' '):
            tableroJuego['down-izq'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'down-med'):
        if(tableroJuego['down-med'] == ' '):
            tableroJuego['down-med'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'down-der'):
        if(tableroJuego['down-der'] == ' '):
            tableroJuego['down-der'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1


def jugadorDos(posicion, tableroJuego):
    if(posicion == 'up-izq'):
        if(tableroJuego['up-izq'] == ' '):
            tableroJuego['up-izq'] = 'O'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'up-med'):
        if(tableroJuego['up-med'] == ' '):
            tableroJuego['up-med'] = 'O'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'up-der'):
        if(tableroJuego['up-der'] == ' '):
            tableroJuego['up-der'] = 'O'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'mid-izq'):
        if(tableroJuego['mid-izq'] == ' '):
            tableroJuego['mid-izq'] = 'O'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'mid-med'):
        if(tableroJuego['mid-med'] == ' '):
            tableroJuego['mid-med'] = 'O'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'mid-der'):
        if(tableroJuego['mid-der'] == ' '):
            tableroJuego['mid-der'] = 'O'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'down-izq'):
        if(tableroJuego['down-izq'] == ' '):
            tableroJuego['down-izq'] = 'O'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'down-med'):
        if(tableroJuego['down-med'] == ' '):
            tableroJuego['down-med'] = 'X'
            return j
        else:
            print("Posicion ocupada")
            return j-1

    if (posicion == 'down-der'):
        if(tableroJuego['down-der'] == ' '):
            tableroJuego['down-der'] = 'O'
            return j
        else:
            print("Posicion ocupada")
            return j-1




    
j=1
for i in range(1,10):
    if j==1:
        print("Turno jugador: "+str(j))
        print("En que posicion desea jugar?")
        posicion = input()
        j=jugadorUno(posicion, tableroJuego)
        imprimirTablero(tableroJuego)
        band = validarX(tableroJuego)
        esGanadorX(band)

        if (j==1):
            j=2
        else:
            j=1
    else:
        print("Turno jugador: "+str(j))
        print("En que posicion desea jugar?")
        posicion = input()
        j=jugadorDos(posicion, tableroJuego)
        imprimirTablero(tableroJuego)
        band = validarO(tableroJuego)
        esGanadorO(band)

        if (j==2):
            j=1
        else:
            j=2
        
if validarX == False and validarO == False:
    print("Empate")



#def elegirPosicion(tableroJuego,posicion):
    

