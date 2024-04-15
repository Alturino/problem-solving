from functools import total_ordering
from typing import List
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        m = {}
        for h in hand:
            m[h] = m.get(h, 0) + 1

        minH = list(m.keys())
        heapq.heapify(minH)
        while minH:
            top = minH[0]
            for i in range(top, top + groupSize):
                if i not in m:
                    return False

                m[i] -= 1
                if m[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True
