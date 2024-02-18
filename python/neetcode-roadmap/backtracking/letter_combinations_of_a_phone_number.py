from typing import List, dataclass_transform


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToCharacters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []

        def combinations(start: int, currStr: str):
            if start >= len(digits):
                res.append(currStr)
                return

            for character in digitToCharacters[digits[start]]:
                combinations(start + 1, currStr + character)

        if digits:
            combinations(0, "")

        return res
