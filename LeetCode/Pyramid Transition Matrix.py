from collections import defaultdict
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)

        mpp = defaultdict(list)
        for a, b, c in allowed:
            mpp[(a, b)].append(c)

        def dfs(s):
            if len(s) == 1:
                return True 

            def helper(i, nxt):
                if i == len(s) - 1: # now no consecutive pairs
                    return dfs(nxt)

                cur_pair = (s[i], s[i + 1])
                if cur_pair not in mpp:
                    return False

                for ch in mpp[cur_pair]:
                    if helper(i + 1, nxt + ch):
                        return True

                return False

            return helper(0, "")

        return dfs(bottom)