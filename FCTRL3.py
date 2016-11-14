testy = int(input())
wynik = []
while testy != 0:
    wejscie = int(input())
    if wejscie == 0:
        wynik1 = "0 1"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 1:
        wynik1 = "0 1"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 2:
        wynik1 = "0 2"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 3:
        wynik1 = "0 6"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 4:
        wynik1 = "2 4"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 5:
        wynik1 = "2 0"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 6:
        wynik1 = "2 0"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 7:
        wynik1 = "4 0"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 8:
        wynik1 = "2 0"
        wynik.append(wynik1)
        testy -= 1
    elif wejscie == 9:
        wynik1 = "8 0"
        wynik.append(wynik1)
        testy -= 1
    else:
        wynik1 = "0 0"
        wynik.append(wynik1)
        testy -= 1
for k in wynik:
    print(k)
