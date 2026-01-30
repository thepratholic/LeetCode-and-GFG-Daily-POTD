from collections import deque


class Solution:
    def rearrangeQueue(self, q):
        
        n = len(q)
        
            
        half = n // 2
        
        tmp = deque()
        
        for _ in range(half):
            tmp.append(q.popleft())
            
        while tmp:
            q.append(tmp.popleft())
            q.append(q.popleft())