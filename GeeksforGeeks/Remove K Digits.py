class Solution:
    def removeKdig(self, s, k):
        n = len(s)
        
        stack = []
        
        for i in range(n):
            while stack and stack[-1] > s[i] and k > 0:
                stack.pop()
                k -= 1
                
            stack.append(s[i])
            
        while k > 0:
            stack.pop()
            k -= 1
            
        res = "".join(stack).lstrip("0")
        
        return res if res else "0"