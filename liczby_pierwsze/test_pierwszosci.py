
def czy_pierwsza(liczba :int):
    liczba = 25

    if liczba < 2:
        return False
    if liczba %2 == 0 or liczba % 3 ==0 :
        return False

    for i in range(5, int(liczba**0.5) + 1, 6):
        if liczba % i == 0 or liczba % (i+2) == 0:
            return False
    return True
if __name__ == '__main__':

    print(czy_pierwsza(50))
