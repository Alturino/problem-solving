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
        # use set to optimize the checking of item is already in permutation or not
        # permutation = set()
        permutation = []

        def permute():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for i in range(len(nums)):
                if nums[i] in permutation:
                    continue

                # permutation.add(nums[i])
                permutation.append(nums[i])
                permute()
                permutation.pop()

        permute()
        return res


s = Solution()
print(s.permute([1, 2, 3]))
