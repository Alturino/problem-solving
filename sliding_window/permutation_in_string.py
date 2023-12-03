class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}

        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1


s = Solution()
# print(s.checkInclusion("ab", "eidbaooo"))
print(s.checkInclusion("ab", "eidboaoo"))
