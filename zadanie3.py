def sortuj_przez_bombelki():
    dane = [1, 6, 5, 8, 2]
    n = len(dane)
    porownania = 0
    zmiany = 0
    for i in range(0, n-1):

        for j in range(0, n-1-i):
            porownania +=1
            if dane[j] < dane[j+1]:
                dane[j], dane[j+1] = dane[j+1], dane[j]
                zmiany +=1
        print(dane)
    print(porownania, zmiany)
if __name__ == '__main__':
    sortuj_przez_bombelki()