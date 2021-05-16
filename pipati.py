def ppt(jugada_j1,jugada_j2):
    opciones = ('piedra', 'papel','tijeras')

    if jugada_j1 in str(opciones):
        j1 = opciones.index(jugada_j1)+1
    else:
        raise NameError('Elige una opcion valida')
    
    if jugada_j2 in str(opciones):
        j2 = opciones.index(jugada_j2)+1
    else:
        raise NameError('Elige una opcion valida')

    if j1 == j2:
        print ('empate')
    if j1 == 1:
        if j2 == 2:
            print('el jugador 2 ha ganado')
        elif j2 == 3:
            print('el jugador 1 ha ganado')
    if j1 == 2:
        if j2 == 1:
            print('el jugador 1 ha ganado')
        elif j2 == 3:
            print('el jugador 2 ha ganado')
    if j1 == 3:
        if j2 == 1:
            print('el jugador 2 ha ganado')
        elif j2 == 2:
            print('el jugador 1 ha ganado')


if __name__=='__main__':
    jugada_j1 = input('Jugador 1, elige: piedra, papel o tijeras: ')
    jugada_j1.lower()
    
    jugada_j2 = input('Jugador 2, elige: piedra, papel o tijeras: ')
    jugada_j2.lower()

    ppt(jugada_j1,jugada_j2)