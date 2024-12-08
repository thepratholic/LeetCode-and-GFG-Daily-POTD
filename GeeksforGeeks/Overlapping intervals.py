class Solution:
    def mergeOverlap(self, arr):
        arr.sort()

        n = len(arr)

        ans = []

        i = 0

        for interval in arr:
            if len(ans) == 0:
                ans.append(interval)
            else:
                if ans[i][1] > interval[1]:
                    continue
                elif ans[i][1] >= interval[0]:
                    ans[i][1] = interval[1]
                else:
                    ans.append(interval)
                    i += 1
        return ans