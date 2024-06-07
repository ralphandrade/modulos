from datetime import date

# função menu

def exibir_menu():
    print('1 - Calcular quadrilatero')
    print('2 - Calcular circulo')
    print('3 - Calcular triangulo')
    print('4 - Calcular trapezio')
    print('5 - Sair do programa')

def calcular_quadrilatero(b ,h):
    a = b * h
    return a

# função da circunferência
def calcular_circulo(r):
    a = 3.4 *r**2
    return a

# função triangulo
def calcular_triangulo(b, h):
    a = (b * h) / 2
    return a

#função trapézio
def calcular_trapezio(b_maior, b_menor, h):
    a = (b_maior + b_menor)*h/2
    return a