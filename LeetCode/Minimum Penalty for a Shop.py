class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        pref = [0] * n
        pref[0] = 1 if customers[0] == 'Y' else 0
        for i in range(1, n):
            pref[i] = pref[i - 1] + (1 if customers[i] == 'Y' else 0)


        total_y = pref[-1]

        min_penalty = total_y
        ans = 0
        for i in range(1, n + 1):
            before_y = pref[i - 1]
            after_y = total_y - pref[i - 1]
            before_n = i - before_y

            cur_penalty = before_n + after_y

            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                ans = i

        return ans