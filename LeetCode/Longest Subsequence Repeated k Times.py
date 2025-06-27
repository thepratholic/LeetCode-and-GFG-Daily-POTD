from collections import deque, Counter


class Solution:

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        freq = [c for c, v in Counter(s).items() if v >= k]
        freq = sorted(freq, reverse = True)

        q = deque(freq)

        ans = ""
        while q:
            cur = q.popleft()

            if len(cur) > len(ans):
                ans = cur

            for ch in freq:
                nxt = cur + ch

                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)

        return ans