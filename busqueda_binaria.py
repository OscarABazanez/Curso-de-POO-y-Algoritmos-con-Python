import random

def busqueda_lineal(lista,objetivo):
    match = False
    contador =0
    for elemento in lista: #O(n)
        contador +=1
        if elemento == objetivo:
            match = True
            break
        
    return match, contador


def busqueda_binaria(lista,comienzo,final,objetivo,contador=0):
    contador +=1
    # print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    if comienzo > final:
        return False,contador

    medio = (comienzo + final )//2

    if lista[medio] == objetivo:
        return (True,contador)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista,medio+1,final, objetivo,contador=contador)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo,contador=contador)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])

    encontrado_binaria,contador2 = busqueda_binaria(lista,0, len(lista),objetivo)
    encontrado_lineal, contador= busqueda_lineal(lista,objetivo)

    print(lista)
    print(f'{contador2}El elemento {objetivo} {"esta" if encontrado_binaria else "no esta"} en la lista')
    print(f'{contador} El elemento {objetivo} {"esta" if encontrado_lineal else "no esta"} en la lista')