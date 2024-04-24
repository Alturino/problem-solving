class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split()
        left, right = 0, len(splitted) - 1

        while left <= right:
            splitted[left], splitted[right] = splitted[right], splitted[left]
            left += 1
            right -= 1

        return " ".join(splitted)
