import heapq
from typing import List
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)

        min_heap = []
        max_heap = []

        queries.sort(key = lambda x : x[0])

        j = 0
        usedQueries = 0

        for i in range(n):
            while j < q and queries[j][0] == i:
                heapq.heappush(max_heap, -queries[j][1])
                j += 1

            nums[i] -= len(min_heap)

            while nums[i] > 0 and max_heap and -max_heap[0] >= i:
                ending = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, ending)
                usedQueries += 1
                nums[i] -= 1

            if nums[i] > 0: return -1

            while min_heap and min_heap[0] <= i:
                heapq.heappop(min_heap)

        return q - usedQueries