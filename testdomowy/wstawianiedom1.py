def wstawianie(lista):
    porownania = 0
    zmiany = 0
    for i in range(1,n):
        temp = lista[i]
        j = i-1
        while j>=0 and lista[j]> temp:
            porownania += 1
            zmiany+=1
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = temp
        print("Posortowana lista: ", end=" ")
        print(lista)
    print("Porównania: ", end=" ")
    print(porownania)
    print("Zmiany: ", end=" ")
    print(zmiany)
lista=[5, 3, 8, 2, 1, 7]
n = len(lista)
wstawianie(lista)
