class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)

            temp = 0
            while n:
                lastDigit = n % 10
                lastDigit **= 2
                temp += lastDigit
                n = n // 10
            n = temp

            if n == 1:
                return True

        return False


s = Solution()
print(s.isHappy(n=19))
