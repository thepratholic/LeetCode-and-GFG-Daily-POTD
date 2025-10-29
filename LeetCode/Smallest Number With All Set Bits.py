class Solution:
    def smallestNumber(self, n: int) -> int:

        def check(num):
            return (num & (num + 1)) == 0

        result = n
        while not check(result):
            result += 1

        return result