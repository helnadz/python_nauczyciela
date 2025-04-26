def potega(podstawa, wykladnik):
    if wykladnik==0:
        return 1
    if wykladnik%2==0:
        pol=potega(podstawa,wykladnik//2)
        return pol*pol
    else:
        return potega(podstawa,wykladnik-1)*podstawa
if __name__ == '__main__':
        print(potega(6,10))