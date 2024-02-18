from typing import List


class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     if len(position) == 1:
    #         return 1
    #
    #     cars = [(p, s) for p, s in zip(position, speed)]
    #     cars.sort(key=lambda x: x[0], reverse=True)
    #
    #     st = []
    #     for p, s in cars:
    #         currTime = (target - p) / s
    #         if st and currTime <= st[-1]:
    #             continue
    #         st.append(currTime)
    #     return len(st)

    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     if len(position) == 1:
    #         return 1
    #
    #     cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
    #     cars.sort(key=lambda x: x[0], reverse=True)
    #
    #     result = 0
    #     maxTime = 0.0
    #     for p, time in cars:
    #         if time > maxTime:
    #             maxTime = time
    #             result += 1
    #     return result

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)

        st = []
        for p, s in cars:
            st.append((target - p) / s)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)


s = Solution()
print(s.carFleet(12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
