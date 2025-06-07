import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        pq = []
        
        for i, ch in enumerate(s):
            if ch != '*':
                heapq.heappush(pq, (ch, -i))

            else:
                heapq.heappop(pq)

        return "".join(ch for ch, _ in sorted(pq, key = lambda x : -x[1]))