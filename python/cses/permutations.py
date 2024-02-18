n = int(input())

if n <= 3:
    if n == 1:
        print(1)
    else:
        print("NO SOLUTION")
else:
    res = []
    for i in range(n - int((n % 2 == 0)), 0, -2):
        res.append(i)

    for i in range(n - int((n % 2 == 1)), 1, -2):
        res.append(i)

    print(" ".join(list(map(str, res))))
