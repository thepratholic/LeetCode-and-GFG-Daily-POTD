from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)

        ans = []

        for i in range(0, n, k):
            temp = s[i : i + k]

            if len(temp) < k:
                temp += fill * (k - len(temp))
            ans.append(temp)

        return ans