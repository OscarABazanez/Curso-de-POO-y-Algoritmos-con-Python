import random

def ordenamiento_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        # print(f'Actual {valor_actual} Posicion {posicion_actual}')

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            print(lista)

        lista[posicion_actual] = valor_actual

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))


    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    # lista = [4,3,2,10,12,1,5,6]


    lista_ordenada = ordenamiento_insercion(lista)

    print(lista)
