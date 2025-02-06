from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)

        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                product_map[nums[i] * nums[j]] += 1

        ans = 0

        for k, v in product_map.items():
            if v >= 2:
                comb = (v * (v - 1)) // 2
                ans += comb * 8

        return ans