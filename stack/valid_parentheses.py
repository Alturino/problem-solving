class Solution:
    # def isValid(self, s: str) -> bool:
    #     if len(s) % 2 != 0:
    #         return False
    #
    #     st = []
    #     braces = {"(": ")", "{": "}", "[": "]"}
    #
    #     for c in s:
    #         if c not in braces and not st:
    #             return False
    #
    #         if c in braces:
    #             st.append(c)
    #
    #         if c not in braces:
    #             if braces[st[-1]] == c:
    #                 st.pop()
    #             else:
    #                 return False
    #
    #     return not st

    # def isValid(self, s: str) -> bool:
    #     if len(s) % 2 != 0:
    #         return False
    #
    #     st = []
    #     braces = {")": "(", "]": "[", "}": "{"}
    #
    #     for c in s:
    #         if c in braces:
    #             if len(st) != 0 and braces[c] == st[-1]:
    #                 st.pop()
    #             else:
    #                 return False
    #         else:
    #             st.append(c)
    #
    #     return not st

    # def isValid(self, s: str) -> bool:
    #     if len(s) % 2 != 0:
    #         return False
    #
    #     st = []
    #     braces = {")": "(", "]": "[", "}": "{"}
    #
    #     for c in s:
    #         if c not in braces:
    #             st.append(c)
    #             continue
    #
    #         if not st or st[-1] != braces[c]:
    #             return False
    #
    #         st.pop()
    #     return not st

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        st = []

        for c in s:
            if not st and (c == ")" or c == "}" or c == "]"):
                return False

            if c == ")" and st[-1] == "(":
                st.pop()
            elif c == "}" and st[-1] == "{":
                st.pop()
            elif c == "]" and st[-1] == "[":
                st.pop()
            else:
                st.append(c)

        return not st


s = Solution()
print(s.isValid("({})"))
