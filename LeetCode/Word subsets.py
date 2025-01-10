from collections import defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mpp = defaultdict(int)

        for word in words2:
            for letter in word:
                if letter not in mpp:
                    mpp[letter] = 0
                mpp[letter] = max(mpp[letter], word.count(letter))

        def helper(s1):
            temp = defaultdict(int)
            for ele in s1:
                temp[ele] += 1
            for key,val in mpp.items():
                if key not in temp or temp[key] < mpp[key]:
                    return False
            return True

        res = []
        for word in words1:
            if helper(word):
                res.append(word)

        return res