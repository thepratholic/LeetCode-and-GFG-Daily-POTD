from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        candiesCollected = 0
        visited = set()
        foundBoxes = set()
        
        q = deque()
        for b in initialBoxes:
            foundBoxes.add(b)
            if status[b] == 1:
                q.append(b)
                visited.add(b)
                candiesCollected += candies[b]

        while q:
            box = q.popleft()

            for insideBox in containedBoxes[box]:
                foundBoxes.add(insideBox)
                if status[insideBox] == 1 and insideBox not in visited:
                    q.append(insideBox)
                    visited.add(insideBox)
                    candiesCollected += candies[insideBox]

            for boxKey in keys[box]:
                status[boxKey] = 1
                if boxKey in foundBoxes and boxKey not in visited:
                    q.append(boxKey)
                    visited.add(boxKey)
                    candiesCollected += candies[boxKey]

        return candiesCollected