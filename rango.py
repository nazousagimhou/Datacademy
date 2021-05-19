
def validar(l_sup, l_inf)-> bool:
    if l_sup != l_inf and l_sup > l_inf:
        while True:
            valor = float(input(f'escribe un numero: '))
            if l_sup >= valor and l_inf <= valor:
                print(f'el {valor} esta en el rango {l_sup, l_inf}')
                return True
            else:
                print(f'el {valor}  no esta en el rango {l_sup, l_inf}')
    else:
        print(f'los valores para el rango no son validos')
        return False


if __name__=='__main__':
    l_inf = float(input(f'Escribe el limite inferior de un rango: '))
    l_sup = float(input(f'Escribe el limite superior de un rango: '))

    validar(l_sup,l_inf)