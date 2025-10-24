from typing import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        for num in range(n + 1, 1224445):

            freq = Counter(str(num))

            if all(int(k) == v for k, v in freq.items()):
                return num