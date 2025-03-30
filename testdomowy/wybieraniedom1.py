def wybieranie(lista):
    for i in range (n):
        min=i
        for j in range (i+1,n):
            if lista[j]<lista[min]:
                min=j
        lista[i],lista[min] = lista[min], lista[i]
        print("Uporządkowana: ", end=" ")
        print(lista)
lista=[2, 6, 1, 8, 3, 9]
n=len(lista)
wybieranie(lista)


