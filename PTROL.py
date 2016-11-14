t = int(input())
wyjscie = []
z = ()
while t > 0:
    n = input()
    n = n.split(" ")
    i = n[0:1]
    z = n[1:2]
    n = n[2:] + z
    n = " ".join(n)
    wyjscie.append(n)
    t -= 1
for k in wyjscie:
    print(k)
