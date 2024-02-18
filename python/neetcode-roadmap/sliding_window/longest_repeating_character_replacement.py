class Solution:
    # # Time Complexity O(26N)
    # # Space Complexity O(N)
    # def characterReplacement(self, s: str, k: int) -> int:
    #     count = {}
    #
    #     left = 0
    #     res = 0
    #     for right in range(len(s)):
    #         count[s[right]] = count.get(s[right], 0) + 1
    #
    #         while (right - left + 1) - max(count.values()) > k:
    #             count[s[left]] -= 1
    #             left += 1
    #
    #         res = max(res, right - left + 1)
    #     return res

    # Time Complexity O(N)
    # Space Complexity O(N)
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        maxFrequency = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFrequency = max(maxFrequency, count[s[right]])

            while (right - left + 1) - maxFrequency > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
