"""
Ala ma kota
Ala nie ma kota

ala ma kota
Ala nie ma kota


"""
def porownaj_napisy(napis1,napis2):
    najkrotsza = min(len(napis1), len(napis2))
    for i in range (najkrotsza):
        if napis1[i]<napis2[i]:
            return -(i+1)
        elif napis1[i] > napis2[i]:
            return i+1
    if len(napis1) == len(napis2):
        return 0
    elif len(napis1)< len(napis2):
        return -najkrotsza
    else:
        return najkrotsza
if __name__ == '__main__':
    print(porownaj_napisy("Ala ma kota", "Ala ma kota i psa"))
