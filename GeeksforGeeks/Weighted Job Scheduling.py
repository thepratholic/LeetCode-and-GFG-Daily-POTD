class Solution: 
    def maxProfit(self, jobs):
        
        n = len(jobs)
        jobs.sort()

        def get_next_index(target):
            res = n
            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high) >> 1

                if jobs[mid][0] >= target:
                    res = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return res

        def f(idx):
            if idx >= n:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            not_taken = f(idx + 1)

            nxt = get_next_index(jobs[idx][1]) # starting index, target
            taken = jobs[idx][2] + f(nxt)

            dp[idx] = max(taken, not_taken)
            return dp[idx]

        dp = [-1] * (n + 1)
        return f(0)