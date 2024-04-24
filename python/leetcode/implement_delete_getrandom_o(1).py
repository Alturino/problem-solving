import random
from sys import last_value


class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.map[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            toDeleteIndex, lastValue = self.map[val], self.list[-1]
            self.list[toDeleteIndex], self.map[lastValue] = lastValue, toDeleteIndex
            self.list.pop()
            del self.map[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        range = random.randint(0, len(self.map) - 1)
        return self.list[range]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
