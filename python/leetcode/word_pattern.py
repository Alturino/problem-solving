class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted = s.split()
        if len(pattern) != len(splitted):
            return False

        m = {}
        se = set()
        for i, p in enumerate(pattern):
            if p not in m and splitted[i] not in se:
                m[p] = splitted[i]
                se.add(splitted[i])
            elif p in m and m[p] == splitted[i]:
                continue
            else:
                return False

        return True


s = Solution()
print(s.wordPattern("abba", "dog dog dog dog"))
print(s.wordPattern("abba", "dog cat cat dog"))
print()
