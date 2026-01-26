class Solution:
    def permuteDist(self, arr):
        
        
        n = len(arr)
        res = []
        used = [False] * n

        def backtrack(curr):
            if len(curr) == n:
                res.append(curr[:])
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(arr[i])

                    backtrack(curr)

                    curr.pop()    
                    used[i] = False  

        backtrack([])
        return res