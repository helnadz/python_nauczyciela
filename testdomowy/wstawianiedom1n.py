def sortuj_przez_wstawianie():
    dane = [1, 6, 5, 8, 2]
    n = len(dane)
    porownania = 0
    zmiany = 0
    for i in range(1, n):
        czerwony = dane[i]
        for j in range(0, i):
            porownania += 1
            if czerwony < dane[j]:
                dane.pop(i)
                dane.insert(j, czerwony)
                zmiany +=1
                break
        print(dane)
    print(porownania, zmiany)
if __name__ == '__main__':
    sortuj_przez_wstawianie()