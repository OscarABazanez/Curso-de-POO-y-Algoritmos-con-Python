from typing import Counter


def morral(tamano_morral, pesos, valores,n):
    # Si ya no tengo elementos o espacio en el morral
    if n == 0 or tamano_morral ==0:
        return 0

    # Si el peso del elemento n es Mayor al morral, Pasar al siguiente elemento
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral,pesos,valores,n-1)

    # Tomar la decision si meterlo en el morral
    maximum = max(valores[n-1] + morral(tamano_morral - pesos[n-1], pesos,valores,n-1), morral(tamano_morral,pesos, valores,n-1))

    print('-'*30)
    print(f'{n}) El tamaño del morral es {tamano_morral - pesos[n-1]}/{tamano_morral}')

    print(f'{n}) El máximo es {maximum} con el valor {valores[n-1]} y el peso {pesos[n-1]}')
    return maximum


if __name__ == '__main__':
    
    valores = [60,100,120]
    pesos = [10,20,30]
    tamano_morral = 60
    n = len(valores)
    resultado = morral(tamano_morral,pesos,valores,n)
    print('*'*30)
    print(resultado)
