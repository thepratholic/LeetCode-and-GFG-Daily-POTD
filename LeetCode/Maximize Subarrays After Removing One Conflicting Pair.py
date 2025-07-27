class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        valid = 0

        conflictingPoints = [[] for _ in range(n + 1)]

        for a, b in conflictingPairs:
            a, b = min(a, b), max(a, b)
            conflictingPoints[b].append(a)

        maxConflict = 0
        secondMaxConflict = 0

        extra = [0] * (n + 1)

        for end in range(1, n + 1): 
            for u in conflictingPoints[end]:
                if u >= maxConflict:
                    secondMaxConflict = maxConflict
                    maxConflict = u
                elif u > secondMaxConflict:
                    secondMaxConflict = u

            valid += end - maxConflict
            extra[maxConflict] += maxConflict - secondMaxConflict

        return valid + max(extra)