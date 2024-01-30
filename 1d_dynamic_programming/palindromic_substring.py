class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def isPalindrome(left: int, right: int):
            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            left, right = i, i
            isPalindrome(left, right)

            left, right = i, i + 1
            isPalindrome(left, right)

        return res
