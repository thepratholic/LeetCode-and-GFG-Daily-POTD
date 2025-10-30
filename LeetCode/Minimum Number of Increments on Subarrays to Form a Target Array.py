from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        
        result = 0

        cur, prev = 0, 0

        for i in range(n):
            cur = target[i]
            
            if abs(cur) > abs(prev):
                result += abs(cur - prev)

            prev = cur

        return result