from typing import Counter, List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0, 0]

        freq = Counter(nums)

        for k, v in freq.items():
            if v == 2:
                if ans[0] == 0:
                    ans[0] = k

                elif ans[1] == 0:
                    ans[1] = k

                else:
                    break

        return ans