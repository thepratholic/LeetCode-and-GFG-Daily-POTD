from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        n, m = len(players), len(trainers)

        i, j = 0, 0
        ans = 0
        while i < n and j < m:
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
                j += 1

            else:
                j += 1

        return ans