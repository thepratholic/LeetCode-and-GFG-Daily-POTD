class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        n = len(num)
        l, r = 0, 2

        maxi = float('-inf')

        while r < n:
            
            if (int(num[l]) == int(num[l + 1]) == int(num[l + 2])) and int(num[l]) > maxi:
                ans = ""
                ans += num[l]
                ans += num[l + 1]
                ans += num[l + 2]
                maxi = int(num[l])

            else:
                r += 1
                l += 1

        return ans