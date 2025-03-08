class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        l, r = 0, k - 1

        mini = float('inf')
        whites = 0

        for i in range(k):
            if blocks[i] == "W": whites += 1

        mini = min(mini, whites)

        for i in range(k, n):
            if blocks[i - k] == "W": whites -= 1
            if blocks[i] == "W": whites += 1
            mini = min(mini, whites)
        return mini