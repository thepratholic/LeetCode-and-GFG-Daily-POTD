class Solution:
    def maxSum(self, arr):

        arr.sort()

        n = len(arr)
        max_arrangement = []

        left, right = 0, n - 1
        while left <= right:
            if left == right:
                max_arrangement.append(arr[left])
            else:
                max_arrangement.append(arr[right])
                max_arrangement.append(arr[left])
            left += 1
            right -= 1


        max_sum = 0
        for i in range(1, n):
            max_sum += abs(max_arrangement[i] - max_arrangement[i - 1])


        max_sum += abs(max_arrangement[-1] - max_arrangement[0])

        return max_sum