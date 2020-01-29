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
    if znak == 'p':
        return 1
    elif znak == 'h':
        return 9


regex = re.compile("^[ph]+$")

print("Podaj ciąg białka: ")
bialko = input()

while not regex.match(bialko):
    print("Podano niepoprawne dane, podaj poprawny ciąg białka: ")
    bialko = input()

rozmiar = len(bialko)
tablica = np.zeros((rozmiar, rozmiar), dtype=int)

srodek = int(rozmiar / 2)

# ZACZYNAMY OD ŚRODKA
pozycjax = srodek
pozycjay = srodek
tablica[pozycjax][pozycjay] = zastaplitere(bialko[0])


k = 1
while k < rozmiar:
    kierunek = wyznaczkierunek(ra.randint(1, 4))
    if kierunek == 'dol':
        if tablica[pozycjax+1][pozycjay] == 0 and pozycjax < rozmiar and pozycjay < rozmiar:
            print(f'{k}->w dol')
            pozycjax = pozycjax + 1
            tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
            k += 1
        else:
            print(f'{k}->kierunek {kierunek} zablokowany')
            continue
    elif kierunek == 'gora':
        if tablica[pozycjax-1][pozycjay] == 0 and pozycjax < rozmiar and pozycjay < rozmiar:
            print(f'{k}->do gory')
            pozycjax = pozycjax - 1
            tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
            k += 1
        else:
            print(f'{k}->kierunek {kierunek} zablokowany')
            continue
    elif kierunek == 'prawo':
        if tablica[pozycjax][pozycjay+1] == 0 and pozycjax < rozmiar and pozycjay < rozmiar:
            print(f'{k}->w prawo')
            pozycjay = pozycjay + 1
            tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
            k += 1
        else:
            print(f'{k}->kierunek {kierunek} zablokowany')
            continue
    elif kierunek == 'lewo':
        if tablica[pozycjax][pozycjay-1] == 0 and pozycjax < rozmiar and pozycjay < rozmiar:
            print(f'{k}->w lewo')
            pozycjay = pozycjay - 1
            tablica[pozycjax][pozycjay] = zastaplitere(bialko[k])
            k += 1
        else:
            print(f'{k}->kierunek {kierunek} zablokowany')
            continue

print(tablica)


