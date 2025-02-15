class Solution:
    def can_partition(self, j, i2, target, cur):
        n = len(i2)

        if j == n:
            return cur == target

        for index in range(j, n):
            val = int(i2[j : index + 1])
            if self.can_partition(index + 1, i2, target, cur + val):
                return True

        return False


    def punishmentNumber(self, n: int) -> int:
        ans = 0
        
        for i in range(1, n+1):
            mul = i * i

            if self.can_partition(0, str(mul), i, 0):
                ans += mul

        return ans