from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = "".join(["(", s, ")"])
        tokens = self.parse(s)
        tokens = self.append_zero(tokens)
        rpn = self.toRpn(tokens)
        res = self.evalRPN(rpn)
        return res

    def parse(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            if s[i].isnumeric():
                nums = [s[i]]
                j = i + 1
                while j < len(s) and s[j].isnumeric():
                    nums.append(s[j])
                    j += 1
                i = j - 1
                res.append("".join(nums))
            else:
                res.append(s[i])
            i += 1
        return res

    def append_zero(self, tokens: List[str]) -> List[str]:
        res = []
        for i, token in enumerate(tokens):
            if token == "-" and tokens[i - 1] == "(":
                res.append("0")
            res.append(token)
        return res

    def toRpn(self, tokens: List[str]) -> List[str]:
        res, op = [], []
        for token in tokens:
            if token.isnumeric():
                res.append(token)
            elif token == "(":
                op.append(token)
            elif token == ")":
                while op and op[-1] != "(":
                    res.append(op.pop())
                op.pop()
            else:
                while op and op[-1] != "(":
                    res.append(op.pop())
                op.append(token)

        while op:
            res.append(op.pop())

        return res

    def evalRPN(self, s: List[str]) -> int:
        st = []
        for token in s:
            if token == "+":
                a, b = st.pop(), st.pop()
                st.append(a + b)
            elif token == "-":
                a, b = st.pop(), st.pop()
                st.append(b - a)
            elif token.isnumeric():
                st.append(int(token))
        return st[-1]


s = Solution()
# print(s.calculate("1 + 1"))  # 2
# print(s.calculate(" 2-1 + 2 "))  # 3
# print(s.calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
# print(s.calculate("23 + 432"))  # 455
# print(s.calculate("1-(     -2)"))  # 3
print(s.calculate("-(2 + 3)"))  # -5
print()
