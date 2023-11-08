def towerOfHanoi(n, fromRod, auxRod, toRod):
    if n == 1:
        print("Move disk 1 from rod", fromRod, "to rod ", toRod)
        return
    towerOfHanoi(n - 1, fromRod, toRod, auxRod)
    print("Move disk", n, "from rod", fromRod, "to rod ", toRod)
    towerOfHanoi(n - 1, auxRod, fromRod, toRod)

towerOfHanoi(3, "a", "b", "c")
