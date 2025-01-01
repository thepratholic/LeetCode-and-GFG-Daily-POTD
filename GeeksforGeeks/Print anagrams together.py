from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        #code here

        mpp = defaultdict(list)

        for x in arr:
            temp = "".join(sorted(x))
            mpp[temp].append(x)

        ans = list(mpp.values())
        return ans