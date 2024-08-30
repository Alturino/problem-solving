from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip_address = []
        ip_addresses = []

        def backtracking(start: int = 0):
            if start == len(s) and len(ip_address) == 4:
                ip_addresses.append('.'.join(ip_address))
                return

            if start == len(s) or len(ip_address) == 4:
                return

            segment = []
            for i in range(start, len(s)):
                segment.append(s[i])
                joined_segment = ''.join(segment)
                if (s[start] == '0' and i != start) or segment and int(joined_segment) > 255:
                    break

                ip_address.append(joined_segment)
                backtracking(start=i + 1)
                ip_address.pop()

            return

        backtracking()
        return ip_addresses


s = Solution()
print(s.restoreIpAddresses("25525511135"))

# expected = "255.255.11.135","255.255.111.35"
