n = int(input())
wynik = []
wynik1 = ""
y = 0
while n != 0:
    wejscie = int(input())
    x = wejscie
    wejscie -= 1
    while wejscie != 0:
        x *= wejscie
        wejscie -= 1
    dziesiatki = str(int(x / 10))
    jednosci = str(x % 10)
    wynik1 = dziesiatki + " " + jednosci
    wynik.append(wynik1)
    n -= 1
for k in wynik:
    print(k)
