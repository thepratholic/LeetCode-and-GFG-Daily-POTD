class Solution:
    def countCollisions(self, s: str) -> int:
        n = len(s)
        ans = 0
        stack = []

        for curr in s:
            # when both are moving
            if curr == 'L' and stack and stack[-1] == 'R':
                ans += 2
                stack.pop() 
                while stack and stack[-1] == 'R':
                    ans += 1
                    stack.pop()
                stack.append('S')
            
            elif curr == 'L' and stack and stack[-1] == 'S':
                ans += 1
                stack.append('S')

            elif curr == 'S':
                while stack and stack[-1] == 'R':
                    ans += 1
                    stack.pop()
                stack.append('S')
            
            else:
                stack.append(curr)

        return ans