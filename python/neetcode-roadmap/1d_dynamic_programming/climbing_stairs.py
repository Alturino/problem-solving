class Solution:
    # def climbingStairs(self, n: int) -> int:
    #     if n == 0:
    #         return 1
    #     if n < 0:
    #         return 0
    #     return self.climbingStairs(n - 1) + self.climbingStairs(n - 2)

    # def climbingStairs(self, n: int) -> int:
    #     memo = [-1] * (n + 1)
    #     def climbingStairs(n: int, memo: List[int]) -> int:
    #         if n == 0:
    #             memo[n] = 1
    #             return memo[n]
    #         if n < 0:
    #             return 0
    #         if memo[n] != -1:
    #             return memo[n]
    #         memo[n] = climbingStairs(n - 1, memo) + climbingStairs(n - 2, memo)
    #         return memo[n]
    #     return climbingStairs(n, memo)

    # def climbingStairs(self, n: int) -> int:
    #     memo = [0] * (n + 1)
    #     memo[0] = 1
    #     memo[1] = 1
    #     for i in range(2, n + 1):
    #         memo[i] = memo[i - 1] + memo[i - 2]
    #     return memo[n]

    # def climbingStairs(self, n: int) -> int:
    #     memo = {}
    #     def climbingStairs(n: int, memo) -> int:
    #         if n == 0:
    #             memo[n] = 1
    #             return memo[n]
    #         if n < 0:
    #             return 0
    #         if n in memo:
    #             return memo[n]
    #         memo[n] = climbingStairs(n - 1, memo) + climbingStairs(n - 2, memo)
    #         return memo[n]
    #     return climbingStairs(n, memo)

    # Optimal solution
    def climbingStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


s = Solution()
print(s.climbingStairs(100))
