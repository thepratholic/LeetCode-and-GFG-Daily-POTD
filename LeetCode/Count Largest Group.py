from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = defaultdict(int)

        for number in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(number))
            group[digit_sum] += 1

            maxi = max(group.values())

        return sum(1 for s in group.values() if s == maxi)