def sortuj_przez_wybieranie():

    dane = [1, 6, 5, 8, 2]
    n = len(dane)
    porownania = 0
    zmiany = 0
    for i in range(n):
        pozycja = i
        minimum = dane[i]
        for j in range(i+1, n):
            porownania += 1
            if dane[j] < minimum:
                minimum = dane[j]
                pozycja = j
                zmiany += 1
        if not pozycja == i:
            dane[pozycja], dane[i] = dane[i], dane[pozycja]
        print(dane)
    print (porownania, zmiany)
if __name__ == '__main__':
    sortuj_przez_wybieranie()


