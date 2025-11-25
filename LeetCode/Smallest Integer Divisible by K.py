from collections import deque


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0:
            return -1

        if k == 1:
            return 1

        q = deque()
        q.append((1 % k, 1)) # remainder, length

        while q:
            r, l = q.popleft()

            if r == 0:
                return l

            else:
                new_r = (r * 10 + 1) % k
                q.append((new_r, l + 1))

        return -1