class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        n = len(v1)
        m = len(v2)

        if n < m:
            v1 += ['0'] * (m - n)
        else:
            v2 += ['0'] * (n - m)

        for a, b in zip(v1, v2):
            x, y = int(a), int(b)

            if x < y:
                return -1

            elif x > y:
                return 1

        return 0