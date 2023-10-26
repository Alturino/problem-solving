from typing import List


class Solution:
    def permutate(self, nums:List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]] # deep copy of the nums
        
        for i in range(len(nums)):
            n = nums.pop(0)

            permutations = self.permutate(nums)

            for permutation in permutations:
                permutation.append(n)
            res.extend(permutations)
            nums.append(n)
        return res

s = Solution()
print(s.permutate([1,2,3]))
