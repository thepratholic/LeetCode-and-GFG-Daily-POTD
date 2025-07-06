from typing import Counter, List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.mpp = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        self.mpp[self.nums2[index]] -= 1
        if self.mpp[self.nums2[index]] == 0:
            del self.mpp[self.nums2[index]]

        self.nums2[index] += val
        self.mpp[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for i in range(len(self.nums1)):
            if (tot - self.nums1[i]) in self.mpp:
                ans += self.mpp[tot - self.nums1[i]]

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)