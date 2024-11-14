#User function Template for python3
import heapq
class Solution:
    def nearlySorted(self, arr, k):
        #code
        n = len(arr)

        heap = arr[:k+1]
        heapq.heapify(heap)
        target_index = 0

        for i in range(k+1, n):

            arr[target_index] = heapq.heappop(heap)
            target_index += 1
            heapq.heappush(heap, arr[i])

        while heap:
            arr[target_index] = heapq.heappop(heap)
            target_index += 1