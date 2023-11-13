from typing import List


def efficientShipping(boxes: List[int], unitsPerBox: List[int], truckSize: int) -> int:
    maxUnit = 0
    currSize = 0
    currMax = 0
    for i, v in enumerate(boxes):
        currSize += v
        if currSize <= truckSize:
            currMax += boxes[i] * unitsPerBox[i]
            maxUnit = max(maxUnit, currMax)
    return maxUnit


print(efficientShipping([1, 2, 3], [3, 2, 1], 3))
