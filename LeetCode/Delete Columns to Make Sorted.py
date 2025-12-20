from typing import DefaultDict, List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)

        mpp = DefaultDict(list)

        for i in range(n):

            for j in range(len(strs[i])):
                ch = strs[i][j]

                mpp[j].append(ch)

        
        ans = 0

        for v in mpp.values():
            l = v

            for i in range(1, len(l)):
                if l[i] < l[i - 1]:
                    ans += 1
                    break

        return ans