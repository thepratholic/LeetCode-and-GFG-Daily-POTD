from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        n = len(folder)

        folder.sort()
        ans = [folder[0]]
        for i in range(1, n):
            last = ans[-1]

            last += "/"

            if not folder[i].startswith(last):
                ans.append(folder[i])

        return ans