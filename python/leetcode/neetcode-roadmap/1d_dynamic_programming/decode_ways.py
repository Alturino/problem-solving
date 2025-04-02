class Solution:
    def numDecodings(self, s: str) -> int:
        prev = prev_2 = 0
        res = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                prev = 0
            else:
                prev = res

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
                prev += prev_2

            prev_2 = res
            res = prev
            prev = 0

        return res

    # def numDecodings(self, s: str) -> int:
    #     dp = {len(s): 1}
    #     for i in range(len(s) - 1, -1, -1):
    #         if s[i] == "0":
    #             dp[i] = 0
    #         else:
    #             dp[i] = dp[i + 1]
    #
    #         if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
    #             dp[i] += dp[i + 2]
    #     return dp[0]

    # def numDecodings(self, s: str) -> int:
    #     cache = {}
    #
    #     def recursive(step: int = 0) -> int:
    #         if step == len(s):
    #             return 1
    #         if s[step] == "0":
    #             return 0
    #         if step in cache:
    #             return cache[step]
    #
    #         res = recursive(step + 1)
    #         if step < len(s) - 1:
    #             if s[step] == "1" or (s[step] == "2" and s[step + 1] < "7"):
    #                 res += recursive(step + 2)
    #         cache[step] = res
    #         return res
    #
    #     return recursive()

    # def numDecodings(self, s: str) -> int:
    #     def recursive(step: int = 0) -> int:
    #         if step == len(s):
    #             return 1
    #         if s[step] == "0":
    #             return 0
    #
    #         res = recursive(step + 1)
    #         if step < len(s) - 1:
    #             if s[step] == "1" or (s[step] == "2" and s[step + 1] < "7"):
    #                 res += recursive(step + 2)
    #         return res
    #
    #     return recursive()
