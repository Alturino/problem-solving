from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for i in range(len(code))]

        n = len(code)
        left, right = 1, k
        res = []
        if k < 0:
            k = -k
            left, right = n - k, n - 1

        suma = sum(code[left : right + 1])
        for i in range(n):
            res.append(suma)
            leftIndex = left % n
            suma -= code[leftIndex]
            left += 1
            right += 1
            rightIndex = right % n
            suma += code[rightIndex]
        return res


s = Solution()
print(s.decrypt(code=[5, 7, 1, 4], k=3))
