class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        length = 0
        bits = k.bit_length()

        sum_ = 0
        pos = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if pos < bits and sum_ + (1 << pos) <= k:
                    sum_ += 1 << pos
                    length += 1

            else:
                length += 1
            pos += 1
        return length