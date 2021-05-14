
def area_triangulo(b,h):
    return (b*h)/2

if __name__=='__main__':
    b = float(input(f'La base de mi triangulo es de: '))
    h = float(input(f'La altura de mi triangulo es:  '))
    area = area_triangulo(b,h)

    print(f'el area de mi triangilo es {area} unidades cuadradas')