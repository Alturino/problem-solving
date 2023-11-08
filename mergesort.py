def mergeSort(list, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(list, start, mid)
        mergeSort(list, mid + 1, end)
        merge(list, start, mid, end)


def merge(list, start, mid, end):
    temp = [0] * (end - start + 1)
    i, j, k = start, mid + 1, 0

    while i <= mid and j <= end:
        if list[i] <= list[j]:
            temp[k] = list[i]
            k += 1
            i += 1
        else:
            temp[k] = list[j]
            k += 1
            j += 1

    while i <= mid:
        temp[k] = list[i]
        k += 1
        i += 1

    while j <= end:
        temp[k] = list[j]
        k += 1
        j += 1

    for i in range(start, end + 1):
        list[i] = temp[i - start]


actual = [1, 4, 3, 2, 6, 5, 9, 10]
expected = actual.copy()
expected = sorted(expected)
mergeSort(actual, 0, len(actual) - 1)
print(actual)
print(expected)
