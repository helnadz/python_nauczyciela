def wyszukiwanie(napis1, napis2):
    lista = []
    for i in range(len(napis1)-len(napis2)+1):
        if napis1[i] == napis2[0] or napis2[0] == "*":
            czyPrawda = True
            for j in range(len(napis2)-1):
                if napis2[j+1] == "*": continue
                if napis1[i+j+1] != napis2[j+1]:
                    czyPrawda = False
            if czyPrawda:
                lista.append(i)

    return lista
if __name__ == '__main__':

    napis1 = "ala ma kotaka"
    napis2 = "a*a"
print(wyszukiwanie(napis1, napis2))