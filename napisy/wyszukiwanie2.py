def wyszukaj_naiwnie(sprawdzany, szukany):
    for i in range(len(sprawdzany) - len(szukany) + 1):
        znaleziono = True
        for j in range(len(szukany)):
            if not sprawdzany[i+j]==szukany[j]:
               znaleziono = False
               break
        if znaleziono:
               return i

    return None


if __name__ == '__main__':
    sprawdzany = "Ala ma koguta kota i psa"
    szukany = "kota"
    print(wyszukaj_naiwnie(sprawdzany, szukany))