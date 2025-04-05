def sortuj_parzyste(dane):
    n = len(dane)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if dane[j]%2 > dane[j + 1]%2:
                dane[j], dane[j + 1] = dane[j + 1], dane[j]
def sortuj(dane):
    n = len(dane)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if dane[j] > dane[j + 1]:
                dane[j], dane[j + 1] = dane[j + 1], dane[j]
if __name__ == '__main__':
    dane = [2, 83, 77, 5, 12, 43, 67, 44]
    sortuj(dane)
    sortuj_parzyste(dane)

    print(dane)