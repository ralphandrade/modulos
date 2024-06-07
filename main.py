# Importar modulo
import os
from modulos import *

# programa principal
if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input("Opção desejada: ")

        match opcao:
            case '1':
                b = int(input('Base do quadrilatero: '))
                h = int(input('Altura do quadrilatero: '))
                print(f'Area: {calcular_quadrilatero(b, h)}')
                continue
            case'2':
                r = int(input('Raio do circulo: '))
                print(f'Area : {calcular_circulo(r)}')
                continue
            case'3':
                b = int(input('Base do triangulo: '))
                h = int(input('Altura do triangulo: '))
                print(f'Area: {calcular_triangulo(b, h)}')
                continue
            case'4':
                b_maior = int(input('b_maior: '))
                b_menor = int(input('b_menor: '))
                h = int(input('altura do trapezio: '))
                print(f'Area: {calcular_trapezio(b_maior, b_menor, h)}')
                continue
            case'5':
                print('Programa encerrado')
                break

