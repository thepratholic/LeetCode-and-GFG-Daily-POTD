from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        unplaced = 0

        unused = [True] * n
        for i in range(n):
            placed = False

            for j in range(n):
                if unused[j] and baskets[j] >= fruits[i]:
                    unused[j] = False
                    placed = True
                    break

            if not placed:
                unplaced += 1

        return unplaced 