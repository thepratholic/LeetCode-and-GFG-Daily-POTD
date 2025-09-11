import heapq


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
        n = len(s)
        t = [''] * n
        pq = []

        for i in range(n):
            if s[i] not in vowels:
                t[i] = s[i]

            else:
                heapq.heappush(pq, (ord(s[i]), s[i]))

        
        for i in range(n):
            if t[i] == '':
                ascii_val, ch = heapq.heappop(pq)
                t[i] = ch

        return "".join(t)