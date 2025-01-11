from typing import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False

        count = Counter(s)
        cnt = 0

        for i in count.values():
            cnt += i % 2

        return cnt <= k