from typing import List


class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #
    #     def permutate(start):
    #         if start >= len(nums):
    #             res.append(nums.copy())
    #             return
    #         for i in range(start, len(nums)):
    #             nums[i], nums[start] = nums[start], nums[i]
    #             permutate(start + 1)
    #             nums[i], nums[start] = nums[start], nums[i]
    #
    #     permutate(0)
    #     return res

    # def permutate(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #
    #     if len(nums) == 1:
    #         return [nums[:]]  # deep copy of the nums
    #
    #     for i in range(len(nums)):
    #         n = nums.pop(0)
    #
    #         permutations = self.permutate(nums)
    #
    #         for permutation in permutations:
    #             permutation.append(n)
    #         res.extend(permutations)
    #         nums.append(n)
    #     return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = []
        used = set()

        def backtracking(start: int = 0):
            if len(permutations) == len(nums):
                res.append(permutations.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    permutations.append(nums[i])

                    backtracking(i + 1)

                    used.remove(nums[i])
                    permutations.pop()

        backtracking()
        return res


s = Solution()
print(s.permute([1, 2, 3]))
