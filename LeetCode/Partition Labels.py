from collections import defaultdict
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        mpp = defaultdict(int)

        for i in range(n):
            mpp[s[i]] = i

        size, end = 0, -1

        ans = []
        for i in range(n):
            size += 1
            end = max(end, mpp[s[i]])

            if i == end:
                ans.append(size)
                size = 0
        return ans