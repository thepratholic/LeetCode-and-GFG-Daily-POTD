from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        fruit_diff = Counter()
        min_value = float('inf') 

        for fruit in basket1:
            fruit_diff[fruit] += 1
            min_value = min(min_value, fruit)
        
        for fruit in basket2:
            fruit_diff[fruit] -= 1
            min_value = min(min_value, fruit)

        to_swap = []
        for fruit, count in fruit_diff.items():
            if count % 2 != 0:
                return -1  
            to_swap.extend([fruit] * (abs(count) // 2))

        if not to_swap:
            return 0  

        to_swap.sort()
        n = len(to_swap) // 2

        cost = 0
        for i in range(n):

            cost += min(to_swap[i], 2 * min_value)

        return cost
