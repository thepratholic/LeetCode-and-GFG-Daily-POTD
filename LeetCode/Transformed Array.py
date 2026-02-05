from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = []

        for i, value in enumerate(nums):
            if nums[i] == 0:
                result.append(value)
            
            else:
                if nums[i] < 0:
                    new_idx = (abs(i) + value) % n
                    result.append(nums[new_idx])

                else:
                    new_idx = (abs(i) + value) % n
                    result.append(nums[new_idx])

        return result