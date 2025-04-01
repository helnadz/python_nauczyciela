def sortuj_napisy(dane):
    n = len(dane)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(dane[j]) > len(dane[j + 1]):
                dane[j], dane[j + 1] = dane[j + 1], dane[j]

if __name__ == '__main__':
    dane = ["ala", "kotek", "pies", "droga", "informatyka"]
    sortuj_napisy(dane)
    print(dane)