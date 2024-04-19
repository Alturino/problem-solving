import heapq
from typing import List


def h_index(citations: List[int]) -> List[int]:
    minH = []
    ans = []
    hIndex = 0
    for i, citation in enumerate(citations):
        if citation > hIndex:
            heapq.heappush(minH, citation)
        while minH and minH[0] <= hIndex:
            heapq.heappop(minH)
        if len(minH) >= hIndex + 1:
            hIndex += 1
        ans.append(hIndex)
    return ans


# def h_index(citations: List[int]) -> List[int]:
#     dq = collections.deque()
#     ans = []
#     hIndex = 0
#     for i, citation in enumerate(citations):
#         if citation > hIndex:
#             dq.append(citation)
#         while dq and dq[0] <= hIndex:
#             dq.popleft()
#         if len(dq) >= hIndex + 1:
#             hIndex += 1
#         ans.append(hIndex)
#     return ans


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    papers = list(map(int, input().split()))
    hIndex = list(map(str, h_index(papers)))
    output = " ".join(hIndex)
    print(f"Case #{i}: {output}")


# print(h_index([1, 3, 3, 2, 2, 15]))
# print(h_index([5, 1, 2]))
# print()
