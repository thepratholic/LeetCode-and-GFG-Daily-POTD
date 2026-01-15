from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        vmax, vcur = 1, 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                vcur += 1

            else:
                vmax = max(vmax, vcur)
                vcur = 1

        hmax, hcur = 1, 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                hcur += 1

            else:
                hmax = max(hmax, hcur)
                hcur = 1
        vmax = max(vmax, vcur)
        hmax = max(hmax, hcur)

        side = min(hmax, vmax) + 1
        return side * side