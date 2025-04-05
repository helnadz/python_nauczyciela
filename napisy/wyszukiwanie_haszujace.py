def haszowanie(sprawdzany, szukany):
    suma = 0
    suma_szukany = 0

    for i in range(len(szukany)):

        suma+=ord(sprawdzany[i])
        suma_szukany+=ord(szukany[i])

    for i in range(len(sprawdzany) - len(szukany)+1):
        if suma==suma_szukany:
            znaleziono = True
            for j in range(len(szukany)):
                if not sprawdzany[i+j]==szukany:
                    znaleziony=False
                    break
            if znaleziono:
                return i
        suma-=ord(sprawdzany[i])
        suma+=ord(sprawdzany[i+len(szukany)])
    return None
if __name__ == '__main__':
    sprawdzany = "Ala ma koguta kota i psa"
    szukany = "kota"
    print(haszowanie(sprawdzany, szukany))