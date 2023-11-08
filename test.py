# this code is from this video https://www.youtube.com/watch?v=ngCos392W4w
# def sum(n: int) -> int:
#     if n <= 0:
#         return 0
#     return sum(n - 1) + n
#
# print(sum(3))

# def find_ways(n:int, m:int) -> int:
#     if n == 1 or m == 1:
#         return 1
#     return find_ways(n - 1, m) + find_ways(n, m - 1)
# print(find_ways(3, 3))

# def count_partitions(n: int, m: int) -> int:
#     if n == 0:
#         return 1
#     if m == 0 or n < 0:
#         return 0
#     return count_partitions(n - m, m) + count_partitions(n, m - 1)
# print(count_partitions(9, 5))

from typing import List, Tuple


def partitionDumbellWeight(weights: List[int]) -> List[Tuple[int]]:
    
