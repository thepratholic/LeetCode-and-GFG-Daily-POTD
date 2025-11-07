class Solution:
    def check(self, mid, diff, r, k, n):
        tempDiff = diff[:]
        cumSum = 0 

        for i in range(n):
            cumSum += tempDiff[i]

            if cumSum < mid:
                need = mid - cumSum
                if need > k:
                    return False

                k -= need
                cumSum += need

                if i + 2 * r + 1 < n:
                    tempDiff[i + 2 * r + 1] -= need 

        return True

    def maxPower(self, stations, r, k):
        n = len(stations)
        diff = [0] * n

        for i in range(n):
            diff[max(0, i - r)] += stations[i]
            if i + r + 1 < n:
                diff[i + r + 1] -= stations[i]

        left = min(stations)
        right = sum(stations) + k
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if self.check(mid, diff, r, k, n):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
