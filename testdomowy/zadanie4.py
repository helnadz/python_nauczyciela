def wyszukiwanie(napis1, napis2):
    lista = []
    for i in range(len(napis1)):
        if napis1[i] == napis2:
            lista.append(i)
    return lista
if __name__ == '__main__':

    napis1 = "Ala ma kota"
    napis2 = "a"
print(wyszukiwanie(napis1, napis2))
