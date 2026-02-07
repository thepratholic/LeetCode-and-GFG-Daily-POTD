class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        
        prefix_b = [0] * n
        suffix_a = [0] * n
        prefix_b[0] = 1 if s[0] == 'b' else 0
        suffix_a[n - 1] = 1 if s[n - 1] == 'a' else 0

        for i in range(1, n):
            prefix_b[i] = prefix_b[i - 1] + (s[i] == 'b')

        for i in range(n - 2, -1, -1):
            suffix_a[i] = suffix_a[i + 1] + (s[i] == 'a')

        ans = suffix_a[0]
        for i in range(n - 1):
            ans = min(ans, prefix_b[i] + suffix_a[i + 1])

        ans = min(ans, prefix_b[n - 1])

        return ans