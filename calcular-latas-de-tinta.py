"""
Calcular a quantidade de latas de tinta para pintar uma parede.
"""

litros_lata = int(input('A lata de tinta possui quantos litros?: '))
altura = int(input('Quantos metros tem a parede?: '))
largura = int(input('Qual é a largura da parede: '))

def calculo_tinta():
    area = altura * largura
    total = area / litros_lata
    print(f'Voce vai precisar de {total} latas de tinta.')

calculo_tinta()
