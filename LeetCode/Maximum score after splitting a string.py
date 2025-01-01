class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        maxi = float("-inf")

        n = len(s)

        for i in range(1, n):
            cnt = 0
            left = s[:i]
            right = s[i:]
            cnt += left.count("0")
            cnt += right.count("1")
            maxi = max(maxi, cnt)

        return maxi