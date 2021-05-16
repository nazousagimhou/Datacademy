def convertidor (unidades, distancia):
    if unidades == 0:
        distancia_0 = distancia* 1.609344 
        print(f'La distancia en kilometros es : {distancia_0}')
        return distancia_0
    else:
        distancia_1 = distancia* 0.62137119 
        print(f'La distancia en millas es : {distancia_1}')
        return distancia_1


if __name__=='__main__':
    unidades = int(input(f'¿Comvertir distancia de: (0) millas a kilometros o (1) kilometros a millas? : '))
    distancia = float(input(f'¿Cual es la distancia?: '))
    distancia_final = convertidor(unidades, distancia)
    print(f'la distancia final es: {distancia_final}')