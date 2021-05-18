import math

def volumen_cilindo(radio, haltura_c):
    vol_cil = (4 * math.pi * haltura_c * radio**3)/3
    return vol_cil

def volumen_cubo(arista):
    vol_cubo = arista**3
    return vol_cubo

def volumen_piramide(haltura_p,lado):
    volumen_piramide = (1/3)*haltura_p*lado**2
    return volumen_piramide

if __name__=='__main__':
    figura = int(input(f'¿Cual es la figura? : (0)cilindro , (1)cubo, (2)piramide '))
    volumen = 0

    if figura == 0:
        r_cilindro= float(input(f'¿Cual es el radio del cilindo? : '))
        h_cilindo= float(input(f'¿Cual es la altura del cilindo? : '))
        volumen = volumen_cilindo(r_cilindro, h_cilindo)
        print(f'el volumen es {volumen} unidades cubicas')
    elif figura == 1:
        a_cubo = float(input(f'¿Cual es el tamano de la arista del cubo?: '))
        volumen = volumen_cubo(a_cubo)
        print(f'el volumen es {volumen} unidades cubicas')
    elif figura == 2:
        h_piramide = float(input(f'¿Cual es la altura de la piramide? : '))
        a_piramide = float(input(f'¿Cual es el tamano de la arista de la base?: '))
        volumen = volumen_piramide(h_piramide, a_piramide)
        print(f'el volumen es {volumen} unidades cubicas')
    else:
        raise NameError('Elige una opcion valida: 0  1  2')