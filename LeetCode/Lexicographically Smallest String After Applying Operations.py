from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque([s])
        vis = set()
        smallest = s

        while q:
            cur = q.popleft()

            if cur in vis:
                continue

            vis.add(cur)
            smallest = min(smallest, cur)

            # option 1 : to add a on all odd indices
            l = list(cur)
            n = len(l)
            for i in range(1, n, 2):
                cur_num = l[i]
                cur_num = int(cur_num)
                cur_num = (cur_num + a) % 10
                cur_num = str(cur_num)
                l[i] = cur_num

            added = "".join(l)

            # option 2 : rotate the string by b times
            rotated = cur[-b : ] + cur[ : -b]

            for nxt in [added, rotated]:
                if nxt not in vis:
                    q.append(nxt)

        return smallest