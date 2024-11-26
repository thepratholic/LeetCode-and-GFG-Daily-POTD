def circularSubarraySum(arr):

    def kadane(nums):
        current_max = global_max = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)
        return global_max

    max_norm = kadane(arr)

    total = sum(arr)

    min_norm = kadane([-x for x in arr])

    max_circular = total + min_norm

    if max_norm < 0:
        return max_norm

    return max(max_circular, max_norm)