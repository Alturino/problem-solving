from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        st = []

        def generate(open: int, close: int):
            if open == close == n:
                res.append("".join(st))
                return

            if open < n:
                st.append("(")
                generate(open + 1, close)
                st.pop()

            if close < open:
                st.append(")")
                generate(open, close + 1)
                st.pop()

        generate(0, 0)
        return res


s = Solution()
print(s.generateParenthesis(3))
