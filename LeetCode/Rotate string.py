class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        tmp = goal + goal
        if s in tmp and len(s) == len(goal):
            return True
        else:
            return False