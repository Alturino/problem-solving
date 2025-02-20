class Solution:
    # def getHappyString(self, n: int, k: int) -> str:
    #     res, curr = "", ""
    #     index_in_sorted_list = 0
    #
    #     def backtrack():
    #         nonlocal index_in_sorted_list
    #         nonlocal res
    #         nonlocal curr
    #         if len(curr) == n:
    #             index_in_sorted_list += 1
    #             if index_in_sorted_list == k:
    #                 res = curr
    #             return
    #         for c in ["a", "b", "c"]:
    #             if len(curr) > 0 and curr[-1] == c:
    #                 continue
    #             curr += c
    #             backtrack()
    #             if res != "":
    #                 return
    #             curr = curr[:-1]
    #
    #     backtrack()
    #     return res

    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack(s: str = ""):
            if len(s) == n:
                res.append(s)
                return
            for c in ["a", "b", "c"]:
                if len(s) > 0 and s[-1] == c:
                    continue
                backtrack(s + c)
            return

        backtrack()

        if len(res) < k:
            return ""

        res.sort()
        return res[k - 1]
