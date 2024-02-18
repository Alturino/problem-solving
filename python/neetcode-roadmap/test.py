# ways to sum
# def ways(total: int, k: int) -> int:
#     if total == 0:
#         return 1
#     if total < 0 or k <= 0:
#         return 0
#     return ways(total - k, k) + ways(total, k - 1)
#
#
# print(ways(8, 2))

# the jungle book
# def minimumGroups()


# def slowestKey(keyTimes):
#     slowest = 0
#     maxTime = 0
#     for i in range(len(keyTimes) - 1, -1, -1):
#         currKey, currTime = keyTimes[i]
#         prevKey, prevTime = keyTimes[i - 1]
#
#         currDeltaTime = currTime - prevTime
#         if maxTime < currDeltaTime:
#             maxTime = currDeltaTime
#             slowest = currKey
#
#     return chr(slowest + ord("a"))
#
#
# # print(slowestKey([(0, 2), (1, 5), (0, 9), (2, 15)]))
# print(
#     slowestKey(
#         [(0, 3), (20, 5), (2, 6), (15, 7), (9, 8), (19, 9), (24, 10), (4, 12), (3, 13)]
#     )
# )


def deret(n: int = 100):
    res = [3]
    exp = [2]
    for i in range(n):
        res.append(res[i] + exp[i])
        exp.append(exp[i] + 2)
    print(res[n - 1])
    print()


<<<<<<< Updated upstream:test.py
deret()


=======
>>>>>>> Stashed changes:python/test.py
# def recursive_random_number_generator(n: int, seed: int = 1) -> int:
#     a = 1103
#     c = 1234
#     m = 1 << 31
#
#     prev = seed
#     res = 0
<<<<<<< Updated upstream:test.py
#     for i in range(100):
=======
#     for i in range(1, n + 1):
>>>>>>> Stashed changes:python/test.py
#         res = ((a * prev) + c) % m
#         prev = res
#
#     return res
#
#
# print(recursive_random_number_generator(100))
# print()
<<<<<<< Updated upstream:test.py

=======
>>>>>>> Stashed changes:python/test.py

# number = 5
# for i in range(10):
#     number *= 2
# print(number)
# print()

# print(bin(13))
# print()
