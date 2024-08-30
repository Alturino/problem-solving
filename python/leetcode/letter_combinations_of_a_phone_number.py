from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        m = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        res = []
        combination = []

        def backtracking(i: int = 0):
            if len(combination) == len(digits):
                res.append("".join(combination))
                return

            for digit in m[int(digits[i])]:
                combination.append(digit)
                backtracking(i + 1)
                combination.pop()

        backtracking()

        return res


s = Solution()
print(s.letterCombinations("2"))
print(s.letterCombinations("23"))
print()
