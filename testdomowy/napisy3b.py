def sortuj_napisy(dane):
    n = len(dane)

    for i in range(0, n-1):

        for j in range(0, n-1-i):

            if dane[j] > dane[j+1]:
                dane[j], dane[j+1] = dane[j+1], dane[j]



if __name__ == '__main__':
    dane=["Ala ma kota", "Ola ma kot", "Ola ma psa"]
    sortuj_napisy(dane)
    print(dane)