t = int(input())
w = t
wyjscie = []
while t > 0:
    wejscie = input()
    z = int(wejscie[0:1])
    wejscie = wejscie[1:]
    p = []
    n = []
    k = 3
    j = 1
    s = z
    while z > 0:
        if z % 2 != 0:
            h = len(wejscie)
            if k < h:
                x = wejscie[k]
                p.append(x)
                y = wejscie[j]
                n.append(y)
                k += 4
                j += 4
                z -= 2
            else:
                y = wejscie[j]
                n.append(y)
                j += 4
                z -= 2
        else:
            x = wejscie[k]
            p.append(x)
            y = wejscie[j]
            n.append(y)
            k += 4
            j += 4
            z -= 2
    t -= 1

    """if s == 1:
        wyjscie.append(p)
    else:
        p = " ".join(p)
        n = " ".join(n)
        p = p + " " + n
        wyjscie.append(p)"""
for i in wyjscie:
    print(i)
