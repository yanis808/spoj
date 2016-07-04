testy = int(input())
nwd = []
while testy != 0:
    wejscie = input()
    liczby = wejscie.split(' ')
    a = liczby[0]
    b = liczby[1]
    a = int(a)
    b = int(b)
    if a != b:
        if a > b:
            while b != 0:
                c = a % b
                a = b
                b = c
            nwd.append(a)
        else:
            c = a
            a = b
            b = c
            while b != 0:
                c = a % b
                a = b
                b = c
            nwd.append(a)
    else:
        nwd.append(a)
    testy -= 1
for i in nwd:
    print(i)
