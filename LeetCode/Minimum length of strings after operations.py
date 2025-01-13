from collections import defaultdict

class Solution:
    def minimumLength(self, s: str) -> int:
        mpp = defaultdict(int)
        n = len(s)
        for i in s:
            mpp[i] += 1
        
        to_delete = 0
        for k, v in mpp.items():
            dels = (v - 1) // 2
            to_delete += dels * 2

        return n - to_delete