from collections import deque


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        q = deque()

        ans = 0

        for i in range(numBottles):
            q.append(1)

        
        while len(q) >= numExchange:
            empty = 0

            for i in range(numExchange):
                q.popleft()
                empty += 1

            ans += empty
            q.append(1)

        while q:
            ans += q.popleft()

        return ans