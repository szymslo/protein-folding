import re
import random as ra
import numpy as np
import matplotlib.pyplot as plt


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


def action(tablica, startpoint, rozmiar):
    # ZACZYNAMY OD ŚRODKA
    pozycjax = startpoint
    pozycjay = startpoint
    tablica[pozycjax][pozycjay] = zastaplitere(bialko[0])

    k = 1
    while k < rozmiar:
        kierunek = wyznaczkierunek(ra.randint(1, 4))
        if kierunek == 'dol':
            if rozmiar - 1 > pozycjax + 1 > 0 and rozmiar - 1 > pozycjay > 0:
                if tablica[pozycjax + 1][pozycjay] == 0:
                    print(f'{k}->w dol')
                    pozycjax = pozycjax + 1
                    tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
                    k += 1
                    if tablica[pozycjax][pozycjay] == 9 and tablica[pozycjax - 1][pozycjay] == 9:
                        print('łączenie...')
                        # 8 to dwie czarne połączone
                        tablica[pozycjax][pozycjay] = 8
                        tablica[pozycjax - 1][pozycjay] = 8
                    print(tablica)
                else:
                    print(f'{k}->kierunek {kierunek} zablokowany')
                    continue
            else:
                print(f'{k}-> {kierunek} wyszło poza zakres')
                continue
        elif kierunek == 'gora':
            if rozmiar - 1 > pozycjax - 1 > 0 and rozmiar - 1 > pozycjay > 0:
                if tablica[pozycjax - 1][pozycjay] == 0:
                    print(f'{k}->do gory')
                    pozycjax = pozycjax - 1
                    tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
                    k += 1
                    if tablica[pozycjax][pozycjay] == 9 and tablica[pozycjax + 1][pozycjay] == 9:
                        print('łączenie...')
                        # 8 to dwie czarne połączone
                        tablica[pozycjax][pozycjay] = 8
                        tablica[pozycjax + 1][pozycjay] = 8
                    print(tablica)
                else:
                    print(f'{k}->kierunek {kierunek} zablokowany')
                    continue
            else:
                print(f'{k}-> {kierunek} wyszło poza zakres')
                continue
        elif kierunek == 'prawo':
            if rozmiar - 1 > pozycjax > 0 and rozmiar - 1 > pozycjay + 1 > 0:
                if tablica[pozycjax][pozycjay + 1] == 0:
                    print(f'{k}->w prawo')
                    pozycjay = pozycjay + 1
                    tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
                    k += 1
                    if tablica[pozycjax][pozycjay] == 9 and tablica[pozycjax][pozycjay - 1] == 9:
                        print('łączenie...')
                        # 8 to dwie czarne połączone
                        tablica[pozycjax][pozycjay] = 8
                        tablica[pozycjax][pozycjay - 1] = 8
                    print(tablica)
                else:
                    print(f'{k}->kierunek {kierunek} zablokowany')
                    continue
            else:
                print(f'{k}->{kierunek} wyszło poza zakres')
                continue
        elif kierunek == 'lewo':
            if rozmiar - 1 > pozycjax > 0 and rozmiar - 1 > pozycjay - 1 > 0:
                if tablica[pozycjax][pozycjay - 1] == 0:
                    print('łączenie...')
                    print(f'{k}->w lewo')
                    pozycjay = pozycjay - 1
                    tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
                    k += 1
                    if tablica[pozycjax][pozycjay] == 9 or 8 and tablica[pozycjax][pozycjay + 1] == 9:
                        # 8 to dwie czarne połączone
                        tablica[pozycjax][pozycjay] = 8
                        tablica[pozycjax][pozycjay + 1] = 8
                    print(tablica)
                else:
                    print(f'{k}->kierunek {kierunek} zablokowany')
                    continue
            else:
                print(f'{k}->{kierunek} wyszło poza zakres')
                continue
    print(tablica)


regex = re.compile("^[ph]+$")

print("Podaj ciąg białka: ")
bialko = input()

while not regex.match(bialko):
    print("Podano niepoprawne dane, podaj poprawny ciąg białka: ")
    bialko = input()

dlugosc = len(bialko)
temp = np.zeros((dlugosc, dlugosc), dtype=int)
srodek = int(dlugosc / 2)

action(temp, srodek, dlugosc)
