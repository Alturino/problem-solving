class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def isPalindrome(left: int, right: int):
            nonlocal res
            nonlocal resLen
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLen = right - left + 1
                if currLen > resLen:
                    res = s[left : right + 1]
                    resLen = currLen
                left -= 1
                right += 1

        for i in range(len(s)):
            left, right = i, i
            isPalindrome(left, right)

            left, right = i, i + 1
            isPalindrome(left, right)

        return res
