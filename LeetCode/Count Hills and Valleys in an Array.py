class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        n = len(nums)
        hills = valleys = 0

        for i in range(1, n - 1):

            if nums[i] == nums[i - 1]:
                continue

            left = -1
            for j in range(i - 1, -1, -1):
                if nums[j] != nums[i]:
                    left = j
                    break

            
            right = -1
            for j in range(i + 1, n):
                if nums[j] != nums[i]:
                    right = j
                    break

            if left == -1 or right == -1:
                continue

            if nums[left] < nums[i] and nums[i] > nums[right]:
                hills += 1

            elif nums[left] > nums[i] and nums[i] < nums[right]:
                valleys += 1

        return hills + valleys