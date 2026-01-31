from collections import defaultdict, deque

class kQueues:

    def __init__(self, n, k):
        self.q = defaultdict(deque)
        self.sz = n
        self.cur = 0
        self.k = k
        

    def enqueue(self, x, i):
        
        if self.isFull():
            return
        
        self.q[i].append(x)
        self.cur += 1

    def dequeue(self, i):
        if self.isEmpty(i):
            return -1
            
        val = self.q[i].popleft()
        self.cur -= 1
        return val

    def isEmpty(self, i):
        return len(self.q[i]) == 0
        
        
    def isFull(self):
        return self.cur == self.sz
