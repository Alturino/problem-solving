from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for triplet in triplets:
            x, y, z = triplet[0], triplet[1], triplet[2]
            if x > target[0] or y > target[1] or z > target[2]:
                continue

            for i, v in enumerate(triplet):
                if v == triplet[i]:
                    good.add(i)

        return len(good) == 3
