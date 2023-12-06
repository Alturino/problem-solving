class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s1) > len(s2):
    #         return False
    #
    #     s1Count, s2Count = [0] * 26, [0] * 26
    #
    #     for i in range(len(s1)):
    #         s1Count[ord(s1[i]) - ord("a")] += 1
    #
    #     i, j = 0, 0
    #     while j < len(s2):
    #         s2Count[ord(s2[j]) - ord("a")] += 1
    #
    #         if j - i + 1 == len(s1):
    #             if s1Count == s2Count:
    #                 return True
    #
    #         if j - i + 1 < len(s1):
    #             j += 1
    #         else:
    #             s2Count[ord(s2[i]) - ord("a")] -= 1
    #             i += 1
    #             j += 1
    #
    #     return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[left]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            left += 1

        return matches == 26


s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
# print(s.checkInclusion("ab", "eidboaoo"))
