valorInicial = float(input('Digite o valor inicial: R$'))
rendimento = float(input('Digite o rendimento por período (%): '))
rendimento = (rendimento/100)
contador = 1
calcTotal = float
aporte = float(input('Aporte a cada período: R$'))
periodo = int(input('Total de períodos: '))

while contador <= periodo:
    if contador == 1:
        calcTotal = valorInicial + (valorInicial * rendimento) + aporte
        print(f'\nApós {contador}, períodos(s), o montante será de R${calcTotal:.2f}')
    else:
        print(f'\nApós {contador}, períodos(s), o montante será de R${calcTotal:.2f}')

    contador = contador + 1

    calcTotal = calcTotal + (calcTotal * rendimento) + aporte

valorTotal = calcTotal - valorInicial