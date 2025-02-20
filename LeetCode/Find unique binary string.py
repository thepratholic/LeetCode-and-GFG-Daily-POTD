from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = ""

        for i in range(n):
            ch = "0" if nums[i][i] == "1" else "1"
            res += ch

        return res