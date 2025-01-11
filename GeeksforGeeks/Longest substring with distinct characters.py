class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        longest = 0
        current = 1
        n = len(s)
        char_set = set()

        l, r = 0, 0

        while r < n:

            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            longest = max(longest, r - l + 1)

            r += 1
        return longest