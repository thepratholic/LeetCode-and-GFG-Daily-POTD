class Solution:
    def numOfPairs(self, arr, k):
        d = {}
        cnt = 0

        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for num in arr:
            if num + k in d:
                cnt += d[num + k]

            if num - k in d:
                cnt += d[num - k]

            d[num] -= 1
            if d[num] == 0:
                del d[num]
        return cnt

s = Solution()
print(s.numOfPairs([1, 5, 3, 4, 2], 3))