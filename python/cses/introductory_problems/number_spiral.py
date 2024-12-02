def number_spiral(row: int, col: int) -> int:
    layer = max(row, col)
    maxNumberInLayer = layer * layer
    previousMaxNumberInLayer = (layer - 1) * (layer - 1)

    # if the layer is even then the max value is located in the bottomest row
    if layer % 2 == 0:
        # if the col > row then we just need to add the previous max number with the row
        if col > row:
            return previousMaxNumberInLayer + row
        # if the row > col then we just need to subtract the max number in this layer with the col + 1
        else:
            return maxNumberInLayer - col + 1
    # if the layer is odd then the max value is on the endest col
    else:
        # if the col > row then we just need to subtract the max number in this layer with row + 1
        if col > row:
            return maxNumberInLayer - row + 1
        # if the row > col then we just need to add the previous max number with the col
        else:
            return previousMaxNumberInLayer + col


t = int(input())
while t:
    row, col = map(int, input().split(" "))
    res = number_spiral(row, col)
    print(res)
    t -= 1
