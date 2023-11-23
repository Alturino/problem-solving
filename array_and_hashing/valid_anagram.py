class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     stemp = sorted(s)
    #     ttemp = sorted(t)
    #
    #     print(stemp, ttemp)
    #     return stemp == ttemp

    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #
    #     ms, mt = {}, {}
    #
    #     for i in range(len(s)):
    #         ms[s[i]] = ms.get(s[i], 0) + 1
    #         mt[t[i]] = mt.get(t[i], 0) + 1
    #
    #     return ms == mt

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        st = {}

        for i in range(len(s)):
            st[s[i]] = st.get(s[i], 0) + 1
            st[t[i]] = st.get(t[i], 0) - 1

        for i in st.values():
            if i != 0:
                return False

        return True


s = Solution()
print(s.isAnagram(s="anagram", t="nagaram"))
