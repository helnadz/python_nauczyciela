import wstawianie
import wybieranie
import bombelki

if __name__ == '__main__':

    dane = [1, 6, 5, 8, 2]
    wstawianie.sortuj_przez_wstawianie(dane)
    wybieranie.sortuj_przez_wybieranie(dane)
    bombelki.sortuj_przez_bombelki(dane)
    print(dane)
