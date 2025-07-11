
class Solution:
    def maxFreeTime(self, endpoint: int, st: list[int], et: list[int]) -> int:
        n = len(st)

        free = [st[0]]
        for i in range(1, n):
            free.append(st[i] - et[i - 1])
        free.append(endpoint - et[-1])  

        m = len(free)
        pre = [0] * m
        suf = [0] * m

        pre[0] = free[0]
        for i in range(1, m):
            pre[i] = max(pre[i - 1], free[i])

        suf[-1] = free[-1]
        for i in range(m - 2, -1, -1):
            suf[i] = max(suf[i + 1], free[i])

        mx = 0
        for i in range(n):
            cur_time = et[i] - st[i]

            prev_end = 0 if i == 0 else et[i - 1]
            next_st = endpoint if i == n - 1 else st[i + 1]

            prev_free = st[i] - prev_end
            next_free = next_st - et[i]

            total_gap = prev_free + next_free
            mx = max(mx, total_gap)

            max_outside = 0
            if i > 0:
                max_outside = max(max_outside, pre[i - 1])
            if i + 2 < m:
                max_outside = max(max_outside, suf[i + 2])

            if max_outside >= cur_time:
                extended = total_gap + cur_time
                mx = max(mx, extended)

        return mx