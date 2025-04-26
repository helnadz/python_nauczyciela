import math
def indeksy_klucza(klucz):
    posortowany_klucz = sorted(klucz)
    return[posortowany_klucz.index(znak) for znak in klucz]
print(indeksy_klucza("pies"))
def szyfruj(napis,klucz):
    kolumny = len(klucz)
    wiersze = math.ceil(len(napis)/len(klucz))
    rozmiar = kolumny*wiersze
    wiadomosc = napis+"_"*(rozmiar - len(napis))
    kolejnosc = indeksy_klucza(klucz)
    zaszyfrowana_wiadomosc = ""
    for wiersz in range(wiersze):
        poczatek = wiersz*len(klucz)
        koniec = (wiersz+1)*len(klucz)
        linia = wiadomosc[poczatek:koniec]
        zaszyfrowana_linia = ''.join([linia[i] for i in kolejnosc ])
        zaszyfrowana_wiadomosc+=zaszyfrowana_linia
    print(zaszyfrowana_wiadomosc)
        #zaszyfrowana_linia=[]
        #for i in kolejnosc:
            #zaszyfrowana_linia.append(linia[i])
       # print(linia, zaszyfrowana_linia)
    #print(wiadomosc)

def odszyfruj(napis,klucz):
    pass


def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
if __name__=='__main__':
    print(f(40))

    napis = "eax toćę ksbax khlwex, fhsmws"
    klucz = "pies"

    zaszyfrowany_napis = szyfruj(napis,klucz)
    print(zaszyfrowany_napis)

    odszyfrowany_napis = odszyfruj(zaszyfrowany_napis,klucz)
    #print(odszyfrowany_napis)