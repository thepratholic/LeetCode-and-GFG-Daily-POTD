from typing import List


class Solution:
    def primeTillN(self, n):
        isprime = [1] * (n + 1)

        ans = []

        for i in range(2, n+1):

            if isprime[i] == 1:

                ans.append(i)                 
                for val in range(i * i, n + 1, i):
                    isprime[val] = 0

        return ans

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.primeTillN(right)

        ans = [-1, -1]

        tmp = []
        for i in range(len(primes) - 1, -1, -1):
            if primes[i] >= left:
                tmp.append(primes[i])

            else: break

        mini = float('inf')
        for j in range(len(tmp) - 2, -1, -1):
            if tmp[j] - tmp[j + 1] < mini:
                mini = min(mini, tmp[j] - tmp[j + 1])
                ans[0], ans[1] = tmp[j + 1], tmp[j]

        return ans