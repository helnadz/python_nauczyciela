def wybieranie(lista):
    licznik_porownan = 0
    licznik_zmian = 0
    for i in range (n):
        min= i
        for j in range (i+1,n):
            licznik_porownan += 1
            if lista[j]<lista[min]:
                min=j
                licznik_zmian += 1
        lista[i],lista[min] = lista[min], lista[i]
        print(lista)
    print("Porównania: ", end=" ")
    print(licznik_porownan)
    print("Zmiany:" ,end=" ")
    print(licznik_zmian)

lista=[2, 6, 1, 8, 3, 9]
n=len(lista)
wybieranie(lista)