class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or = 0
        ans = []
        n = len(nums)

        total = 1 << n
        for mask in range(total):
            sub = []
            cur_or = 0
            for i in range(n):

                if mask & (1 << i):
                    cur_or = cur_or | nums[i]
                    sub.append(nums[i])

            ans.append(sub)
            max_or = max(max_or, cur_or)


        count = 0

        for i in range(len(ans)):

            curList = ans[i]
            orr = 0

            for element in curList:
                orr |= element

            if orr == max_or:
                count += 1

        return count        