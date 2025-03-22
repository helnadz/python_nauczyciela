def sortuj_przez_wstawianie(dane):
    n = len(dane)
    for i in range(1, n):
        czerwony = dane[i]
        for j in range(0, i):
            if czerwony < dane[j]:
                dane.pop(i)
                dane.insert(j, czerwony)
                break
