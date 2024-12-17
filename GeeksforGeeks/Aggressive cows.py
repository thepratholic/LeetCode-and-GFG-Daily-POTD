class Solution:
    def canWePlace(self, nums, mid, cows):
        cntCows = 1
        lastStall = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - lastStall >= mid:
                cntCows += 1
                lastStall = nums[i]
            if cntCows >= cows: return True

        return False

    def aggressiveCows(self, nums, k):
        n = len(nums)
        nums.sort()
        ans = -1
        low, high = 1, max(nums) - min(nums)

        while low <= high:
            mid = (low + high) // 2

            if self.canWePlace(nums, mid, k):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans