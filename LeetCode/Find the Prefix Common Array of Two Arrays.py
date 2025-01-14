
from typing import List
class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        n = len(a)
        c = [0] * n
       
        seen_a = set()
        seen_b = set()

        common_count = 0

        for i in range(n):
            seen_a.add(a[i])
            seen_b.add(b[i])

            if a[i] in seen_b:
                common_count += 1
            
            if b[i] in seen_a:
                common_count += 1

            if a[i] == b[i]:
                common_count -= 1

            c[i] = common_count
        return c