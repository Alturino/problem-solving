class TimeMap:
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int):
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append(tuple([value, timestamp]))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res
