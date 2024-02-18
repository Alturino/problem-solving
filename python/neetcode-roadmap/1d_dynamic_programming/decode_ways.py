class Solution:
    def numDecodings(self, s: str) -> int:
        m = {i + 1: chr(i + ord("a")) for i in range(26)}

        def decode(i: int, currS: str):
            if i >= 27:
                return 0
            if s == "0":
                return 0

            decode(i + 1, s[i + 1])
            decode(i + 2, s[i : i + 1])
