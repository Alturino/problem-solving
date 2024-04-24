from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Pair(index, value/temperature)

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                stIndex, stTemperature = stack.pop()
                res[stIndex] = index - stIndex
            stack.append((index, temperature))

        return res


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
