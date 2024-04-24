from typing import List


class Solution:
    # #  Time Complexity O(N log N)
    # #  Space Complexity O(N)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     m = {}
    #
    #     for num in nums:
    #         m[num] = m.get(num, 0) + 1
    #
    #     sortedm = sorted(m.items(), key=lambda x: x[1], reverse=True)
    #
    #     res = []
    #     for key, v in sortedm:
    #         if len(res) == k:
    #             return res
    #         res.append(key)
    #
    #     return res

    # Time Complexity O(N)
    # Space Complexity O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Count the number of occurence
        for i in nums:
            m[i] = m.get(i, 0) + 1

        for key, v in m.items():
            # Save the count as key and append number to a list that occur key times
            # Save the occurence as key and add the number occur key times to a list
            freq[v].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for key in freq[i]:
                if len(res) == k:
                    return res
                res.append(key)

        return res


s = Solution()
print(s.topKFrequent([1, 2], 2))
