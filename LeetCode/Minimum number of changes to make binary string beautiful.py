class Solution:
    def minChanges(self, s: str) -> int:
        mini_changes_required = 0
        n = len(s)

        for i in range(0, n, 2):
            if s[i] != s[i+1]:
                mini_changes_required += 1
        return mini_changes_required