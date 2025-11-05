from sortedcontainers import SortedList

class Solution:
    def __init__(self):
        self.sum = 0
        self.main = SortedList()
        self.sec = SortedList()

    def insertInSet(self, p, x):
        if len(self.main) < x or p > self.main[0]:
            self.sum += p[0] * p[1]
            self.main.add(p)
            if len(self.main) > x:
                smallest = self.main.pop(0)
                self.sum -= smallest[0] * smallest[1]
                self.sec.add(smallest)
        else:
            self.sec.add(p)

    def removeFromSet(self, p, x):
        if p in self.main:
            self.sum -= p[0] * p[1]
            self.main.remove(p)
            if self.sec:
                largest = self.sec[-1]
                self.sec.remove(largest)
                self.main.add(largest)
                self.sum += largest[0] * largest[1]
        else:
            if p in self.sec:
                self.sec.remove(p)

    def findXSum(self, nums, k, x):
        n = len(nums)
        self.sum = 0
        self.main.clear()
        self.sec.clear()
        result = []
        mp = {}
        i = 0
        j = 0

        while j < n:
            if nums[j] in mp and mp[nums[j]] > 0:
                self.removeFromSet((mp[nums[j]], nums[j]), x)
            mp[nums[j]] = mp.get(nums[j], 0) + 1
            self.insertInSet((mp[nums[j]], nums[j]), x)
            if j - i + 1 == k:
                result.append(self.sum)
                self.removeFromSet((mp[nums[i]], nums[i]), x)
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                else:
                    self.insertInSet((mp[nums[i]], nums[i]), x)
                i += 1
            j += 1
        return result
