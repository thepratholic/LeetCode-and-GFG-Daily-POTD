class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        t = 1

        while True:
            val = num1 - (t * num2)
            if val < t:
                return -1

            min_bits = val.bit_count()
            if min_bits <= t:
                return t
            t += 1