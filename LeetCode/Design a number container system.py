from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.min_indexes = {}
        self.mpp = {}

    def change(self, index: int, number: int) -> None:
        if index in self.mpp:
            prev = self.mpp[index]

            if prev in self.min_indexes:
                self.min_indexes[prev].discard(index)

        self.mpp[index] = number
        if number not in self.min_indexes:
            self.min_indexes[number] = SortedSet()

        self.min_indexes[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.min_indexes or not self.min_indexes[number]:
            return -1

        return next(iter(self.min_indexes[number]))


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)