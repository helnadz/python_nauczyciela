alfabet="aąbcćdeęfghijklłmnopqrsśtuvwxyzźż"
napis = "eax toćę ksbax khlwex, fhsmws"
def odszyfruj(napis, klucz):
    wynik = " "
    for znak in napis:
        if znak in alfabet:
        nowy_indeks=(alfabet.zn


                     )
        wynik+=alfabet[nowy_indeks]
    else:
        wynik+=znak
        return wynik
    for klucz in range(len(alfabet)):
        odszyfrowany_napis=odszyfruj(napis,klucz)

print(f"klucz{klucz}:{odszyfrowany_napis}")



