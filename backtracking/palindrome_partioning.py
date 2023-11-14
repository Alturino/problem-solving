from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def isPalindrome(left: int, right: int):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        def partition(start: int):
            if start >= len(s):
                res.append(part.copy())
                return

            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    part.append(s[start : i + 1])
                    partition(i + 1)
                    part.pop()

        partition(0)
        return res
