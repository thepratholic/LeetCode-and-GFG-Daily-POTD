class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastSeen = [-1] * 3
        cnt = 0
        n = len(s)
        for i in range(n):
            lastSeen[ord(s[i]) - ord('a')] = i
            cnt += (1 + min(lastSeen[0], lastSeen[1], lastSeen[2]))
        return cnt