from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_sum = 0
        for num in derived:
            xor_sum ^= num
        
        # If the XOR sum of all elements is 0, a valid original array exists
        return xor_sum == 0