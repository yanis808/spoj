t = int(input())
wyjscie = []
while t > 0:
    testy = []
    wejscie = input()
    wejscie = wejscie.split(" ")
    n = int(wejscie[0])
    x = int(wejscie[1])
    y = int(wejscie[2])
    for i in range(n):
        if i % x == 0 and i % y != 0:
            i = str(i)
            testy.append(i)
    testy = " ".join(testy)
    wyjscie.append(testy)
    t -= 1
for z in wyjscie:
    print(z)
