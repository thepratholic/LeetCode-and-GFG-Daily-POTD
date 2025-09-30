from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]


        def f(arr):
            newNums = [-1] * (len(arr) - 1)
            for i in range(len(arr) - 1):
                newNums[i] = (arr[i] + arr[i + 1]) % 10

            return newNums

        newArr = f(nums)
        while True:

            if len(newArr) == 1:
                return newArr[0]

            else:
                newArr = f(newArr)
