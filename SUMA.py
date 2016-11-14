try:
    numbers = input()
    sum = []
    x = 0
    while numbers != "":
        numbers = int(numbers)
        x = x + numbers
        sum.append(x)
        numbers = input()
except EOFError:
    for z in sum:
        print(z)
