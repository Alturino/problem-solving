import fileinput

for line in fileinput.input():
    n = int(line)

    res = []
    while n != 1:
        res.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
    res.append(1)
    print(" ".join(map(str, res)))
