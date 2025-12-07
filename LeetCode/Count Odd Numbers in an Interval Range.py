class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        total = high - low + 1

        if high & 1 and low & 1:
            return total // 2 + 1

        else:
            return total // 2