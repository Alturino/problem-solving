class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                windowLen = right - left + 1
                if windowLen < resLen:
                    res = [left, right]
                    resLen = windowLen

                # pop left
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left : right + 1] if resLen != float("infinity") else ""


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
