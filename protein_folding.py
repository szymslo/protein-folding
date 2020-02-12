import re
import random as ra
import numpy as np
import matplotlib.pyplot as plt

biale_wykresX = []
biale_wykresY = []
czarne_wykresX = []
czarne_wykresY = []
wykresX = []
wykresY = []


def wyznaczkierunek(liczba):
    if liczba == 1:
        return "prawo"
    elif liczba == 2:
        return "lewo"
    elif liczba == 3:
        return "gora"
    elif liczba == 4:
        return "dol"


def zastaplitere(znak):
    if znak == 'p':  # biale
        return 1
    elif znak == 'h':  # czarne
        return 9


def sprawdzlitere(znak):
    if znak == 'p':  # biale
        return True
    elif znak == 'h':  # czarne
        return False


def wynik(tab):
    punkty = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            if i >= 1 and j >= 1:
                if tab[i][j] == 9 and tab[i-1][j] == 8:
                    punkty += 1
                if tab[i][j] == 9 and tab[i+1][j] == 8:
                    punkty += 1
                if tab[i][j] == 9 and tab[i][j-1] == 8:
                    punkty += 1
                if tab[i][j] == 9 and tab[i][j+1] == 8:
                    punkty += 1
    return int(punkty*(-1))


def action(rozmiar):
    tablica = np.zeros((rozmiar, rozmiar), dtype=int)
    startpoint = int(rozmiar / 2)

    ostatnie_kierunki = ['brak', 'brak']

    # ZACZYNAMY OD ŚRODKA
    pozycjax = startpoint
    pozycjay = startpoint
    tablica[pozycjax][pozycjay] = zastaplitere(bialko[0])

    wykresX.append(pozycjax)
    wykresY.append(pozycjay)

    if sprawdzlitere(bialko[0]):  # biale
        biale_wykresX.append(pozycjax)
        biale_wykresY.append(pozycjay)
    else:  # czarne
        czarne_wykresX.append(pozycjax)
        czarne_wykresY.append(pozycjay)

    k = 1
    while k < rozmiar:
        kierunek = wyznaczkierunek(ra.randint(1, 4))
        if kierunek == 'dol':
            if ostatnie_kierunki[-1] == 'dol':  # and ostatnie_kierunki[-2] == 'dol':
                print("wymuszenie zmiany kierunku")
                continue
            else:
                if rozmiar - 1 > pozycjax + 1 > 0 and rozmiar - 1 > pozycjay > 0:
                    if tablica[pozycjax + 1][pozycjay] == 0:
                        ostatnie_kierunki.append(kierunek)
                        print(f'{k}->w dol')
                        pozycjax = pozycjax + 1
                        tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
                        k += 1
                        if tablica[pozycjax][pozycjay] == 9 and tablica[pozycjax - 1][pozycjay] == 9:
                            print('łączenie...')
                            # 8 to dwie czarne połączone
                            tablica[pozycjax][pozycjay] = 8
                            tablica[pozycjax - 1][pozycjay] = 8

                        wykresX.append(pozycjax)
                        wykresY.append(pozycjay)

                        if tablica[pozycjax][pozycjay] == 1:
                            biale_wykresX.append(pozycjax)
                            biale_wykresY.append(pozycjay)
                        elif tablica[pozycjax][pozycjay] == 9 or tablica[pozycjax][pozycjay] == 8:
                            czarne_wykresX.append(pozycjax)
                            czarne_wykresY.append(pozycjay)
                    else:
                        print(f'{k}->kierunek {kierunek} zablokowany')
                        continue
                else:
                    print(f'{k}-> {kierunek} wyszło poza zakres')
                    continue
        elif kierunek == 'gora':
            if ostatnie_kierunki[-1] == 'gora':  # and ostatnie_kierunki[-2] == 'gora':
                print("wymuszenie zmiany kierunku")
                continue
            else:
                if rozmiar - 1 > pozycjax - 1 > 0 and rozmiar - 1 > pozycjay > 0:
                    if tablica[pozycjax - 1][pozycjay] == 0:
                        print(f'{k}->do gory')
                        ostatnie_kierunki.append(kierunek)
                        pozycjax = pozycjax - 1
                        tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
                        k += 1
                        if tablica[pozycjax][pozycjay] == 9 and tablica[pozycjax + 1][pozycjay] == 9:
                            print('łączenie...')
                            # 8 to dwie czarne połączone
                            tablica[pozycjax][pozycjay] = 8
                            tablica[pozycjax + 1][pozycjay] = 8

                        wykresX.append(pozycjax)
                        wykresY.append(pozycjay)

                        if tablica[pozycjax][pozycjay] == 1:
                            biale_wykresX.append(pozycjax)
                            biale_wykresY.append(pozycjay)
                        elif tablica[pozycjax][pozycjay] == 9 or tablica[pozycjax][pozycjay] == 8:
                            czarne_wykresX.append(pozycjax)
                            czarne_wykresY.append(pozycjay)
                    else:
                        print(f'{k}->kierunek {kierunek} zablokowany')
                        continue
                else:
                    print(f'{k}-> {kierunek} wyszło poza zakres')
                    continue
        elif kierunek == 'prawo':
            if ostatnie_kierunki[-1] == 'prawo':  # and ostatnie_kierunki[-2] == 'prawo':
                print("wymuszenie zmiany kierunku")
                continue
            else:
                if rozmiar - 1 > pozycjax > 0 and rozmiar - 1 > pozycjay + 1 > 0:
                    if tablica[pozycjax][pozycjay + 1] == 0:
                        print(f'{k}->w prawo')
                        ostatnie_kierunki.append(kierunek)
                        pozycjay = pozycjay + 1
                        tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
                        k += 1
                        if tablica[pozycjax][pozycjay] == 9 and tablica[pozycjax][pozycjay - 1] == 9:
                            print('łączenie...')
                            # 8 to dwie czarne połączone
                            tablica[pozycjax][pozycjay] = 8
                            tablica[pozycjax][pozycjay - 1] = 8

                        wykresX.append(pozycjax)
                        wykresY.append(pozycjay)

                        if tablica[pozycjax][pozycjay] == 1:
                            biale_wykresX.append(pozycjax)
                            biale_wykresY.append(pozycjay)
                        elif tablica[pozycjax][pozycjay] == 9 or tablica[pozycjax][pozycjay] == 8:
                            czarne_wykresX.append(pozycjax)
                            czarne_wykresY.append(pozycjay)
                    else:
                        print(f'{k}->kierunek {kierunek} zablokowany')
                        continue
                else:
                    print(f'{k}->{kierunek} wyszło poza zakres')
                    continue
        elif kierunek == 'lewo':
            if ostatnie_kierunki[-1] == 'lewo':  # and ostatnie_kierunki[-2] == 'lewo':
                print("wymuszenie zmiany kierunku")
                continue
            else:
                if rozmiar - 1 > pozycjax > 0 and rozmiar - 1 > pozycjay - 1 > 0:
                    if tablica[pozycjax][pozycjay - 1] == 0:
                        print('łączenie...')
                        print(f'{k}->w lewo')
                        ostatnie_kierunki.append(kierunek)
                        pozycjay = pozycjay - 1
                        tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
                        k += 1
                        if tablica[pozycjax][pozycjay] == 9 or 8 and tablica[pozycjax][pozycjay + 1] == 9:
                            # 8 to dwie czarne połączone
                            tablica[pozycjax][pozycjay] = 8
                            tablica[pozycjax][pozycjay + 1] = 8

                        wykresX.append(pozycjax)
                        wykresY.append(pozycjay)

                        if tablica[pozycjax][pozycjay] == 1:
                            biale_wykresX.append(pozycjax)
                            biale_wykresY.append(pozycjay)
                        elif tablica[pozycjax][pozycjay] == 9 or tablica[pozycjax][pozycjay] == 8:
                            czarne_wykresX.append(pozycjax)
                            czarne_wykresY.append(pozycjay)
                    else:
                        print(f'{k}->kierunek {kierunek} zablokowany')
                        continue
                else:
                    print(f'{k}->{kierunek} wyszło poza zakres')
                    continue
    print('------------------------------------------')
    print(tablica)
    print('------------------------------------------')
    print(f'PUNKTY: {wynik(tablica)}')
    print('------------------------------------------')
    print('kierunki')
    print(ostatnie_kierunki)


regex = re.compile("^[ph]+$")

print("Podaj ciąg białka: ")
bialko = input()

while not regex.match(bialko):
    print("Podano niepoprawne dane, podaj poprawny ciąg białka: ")
    bialko = input()

dlugosc = len(bialko)

action(dlugosc)

print('------------------------------------------')
print('białe')
print(biale_wykresX)
print(biale_wykresY)
print('------------------------------------------')
print('czarne')
print(czarne_wykresX)
print(czarne_wykresY)
print('------------------------------------------')

plt.plot(wykresY, wykresX, 'k')
plt.plot(biale_wykresY, biale_wykresX, 'co', czarne_wykresY, czarne_wykresX, 'ko', markersize=12)
plt.grid(True)
plt.axis([0, dlugosc, 0, dlugosc])
plt.show()

