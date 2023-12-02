from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token == "+":
                a, b = st.pop(), st.pop()
                result = a + b
                st.append(result)
            elif token == "*":
                a, b = st.pop(), st.pop()
                result = a * b
                st.append(result)
            elif token == "-":
                a, b = st.pop(), st.pop()
                result = b - a
                st.append(result)
            elif token == "/":
                a, b = st.pop(), st.pop()
                result = int(b / a)
                st.append(result)
            else:
                st.append(int(token))

        return st.pop()


s = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(s.evalRPN(tokens))
