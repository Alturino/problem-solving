class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []

        i = 0
        while i < len(path):
            if path[i] == "/":
                if (st and st[-1] != "/") or not st:
                    st.append("/")
            elif path[i] == ".":
                j = i + 1
                dots = [path[i]]
                while j < len(path) and path[j] == ".":
                    dots.append(path[j])
                    j += 1
                word = []
                while j < len(path) and path[j] != "/":
                    word.append(path[j])
                    j += 1
                if word or len(dots) > 2:
                    st.append("".join(dots + word))
                else:
                    if len(dots) == 1 or (len(dots) == 2 and len(st) == 1):
                        i = j - 1
                    elif len(dots) == 2 and len(st) > 1:
                        st.pop()
                        st.pop()
                i = j - 1
            else:
                j = i + 1
                word = [path[i]]
                while j < len(path) and path[j] != "/":
                    word.append(path[j])
                    j += 1
                st.append("".join(word))
                st.append("/")
                i = j
            i += 1

        while len(st) > 1 and st[-1] == "/":
            st.pop()

        return "".join(st)


s = Solution()
print(s.simplifyPath(path="/"))
print(s.simplifyPath(path="//"))
print(s.simplifyPath(path="/home/"))
print(s.simplifyPath(path="/../"))
print(s.simplifyPath(path="/a/a/../"))
print(s.simplifyPath(path="/home/rickyalturino/../"))
print(s.simplifyPath(path="/a/./b/../../c/"))
print(s.simplifyPath(path="/a//a//../"))
print(s.simplifyPath(path="/.../"))
print(s.simplifyPath(path="/..hidden"))
print(s.simplifyPath(path="/.hidden"))
print(s.simplifyPath(path="/.."))
print(s.simplifyPath(path="/a//b////c/d//././/.."))
print()
