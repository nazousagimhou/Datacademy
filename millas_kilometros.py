FACTOR_CONVERSION_KM = 1.609344
FACTOR_CONVERSION_MILLAS = 0.62137119

def convertidor (distancia,constante) -> float:
    return distancia*constante

if __name__=='__main__':
    unidades = int(input(f'¿Comvertir distancia de: (0) millas a kilometros o (1) kilometros a millas? : '))
    
    distancia = float(input(f'¿Cual es la distancia?: '))
    
    if unidades == 0:
        distancia_0 = convertidor(distancia, FACTOR_CONVERSION_KM) 
        print(f'La distancia en kilometros es : {distancia_0}')
    elif unidades == 1:
        distancia_1 =convertidor(distancia, FACTOR_CONVERSION_MILLAS)
        print(f'La distancia en millas es : {distancia_1}')
    else:
        raise NameError('Elige una opcion valida: 0  o 1 ')