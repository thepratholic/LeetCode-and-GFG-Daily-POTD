from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        m = len(capacity)
        total_apples = sum(apple)

        capacity.sort(reverse = True)

        ans = 0
        box_capacity = 0
        for i in range(m):
            if box_capacity >= total_apples: break

            box_capacity += capacity[i]
            ans += 1

        return ans