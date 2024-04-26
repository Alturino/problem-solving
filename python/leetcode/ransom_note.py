class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for c in magazine:
            m[c] = m.get(c, 0) + 1

        for c in ransomNote:
            if c in m and m[c] != 0:
                m[c] -= 1
            else:
                return False
        return True
