from collections import deque


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        q = deque()
        exchange = numExchange

        for i in range(numBottles):
            q.append(1)

        ans = 0

        while len(q) >= exchange:
            empty = 0

            for i in range(exchange):
                q.popleft()
                empty += 1

            ans += empty
            q.append(1)
            exchange += 1

        while q:
            ans += q.popleft()

        return ans