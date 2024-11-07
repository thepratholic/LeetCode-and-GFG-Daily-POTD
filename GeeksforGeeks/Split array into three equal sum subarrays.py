class Solution:
    # Function to determine if array arr can be split into three equal sum sets.
    def findSplit(self, arr):
        total_sum = sum(arr)


        if total_sum % 3 != 0:
            return [-1, -1]

        target = total_sum // 3
        prefix_sum = 0
        first_idx, second_idx = -1, -1


        for i in range(len(arr) - 1):
            prefix_sum += arr[i]


            if prefix_sum == target and first_idx == -1:
                first_idx = i

            elif prefix_sum == 2 * target and first_idx != -1:
                second_idx = i
                break

        if first_idx != -1 and second_idx != -1:
            return [first_idx, second_idx]
        else: return [-1, -1]