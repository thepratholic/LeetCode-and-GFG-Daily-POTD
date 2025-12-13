from typing import List


class Solution:
    def validateCoupons(self, c: List[str], b: List[str], a: List[bool]) -> List[str]:
        ans = []
        n = len(c)

        order = {"electronics": 1,"grocery": 2,"pharmacy": 3,"restaurant": 4}


        def check(s):
            if not s:
                return False
            for ch in s:
                if not (ch.isalnum() or ch == "_"):
                    return False
            return True

        for i in range(n):
            if a[i] and b[i] in order and check(c[i]):
                ans.append((order[b[i]], c[i]))
                
        ans.sort()
        return [c for _, c in ans]
