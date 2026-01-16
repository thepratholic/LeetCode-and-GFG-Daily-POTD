from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        hFences += [1, m]
        vFences += [1, n]
        
        hFences.sort()
        vFences.sort()
        
        hGaps = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                hGaps.add(hFences[j] - hFences[i])
        
        maxSide = -1
        
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                gap = vFences[j] - vFences[i]
                if gap in hGaps:
                    maxSide = max(maxSide, gap)
        
        if maxSide == -1:
            return -1
        
        return (maxSide * maxSide) % MOD
