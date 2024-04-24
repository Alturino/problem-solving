class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed, curr = 0, x
        while curr:
            lastDigit = curr % 10
            reversed = reversed * 10 + lastDigit
            curr //= 10

        return reversed == x
