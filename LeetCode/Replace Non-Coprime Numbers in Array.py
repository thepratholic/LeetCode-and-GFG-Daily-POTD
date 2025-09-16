from math import gcd, lcm
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            stack.append(num)

            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                x = stack.pop()
                y = stack.pop()

                stack.append(lcm(x, y))

        return stack