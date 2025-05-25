from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mpp = defaultdict(int)        
        ans = 0
        for word in words:
            rev = word[::-1]
            if mpp[rev] > 0:
                ans += 4
                mpp[rev] -= 1
            else:
                mpp[word] += 1

        for k, v in mpp.items():
            if k[0] == k[1] and v > 0:
                ans += 2
                break

        return ans