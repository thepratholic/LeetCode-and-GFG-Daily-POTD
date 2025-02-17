class Solution:
    def helper(self, tiles, ans, cur, used):
        if cur:
            ans.add(cur)
            

        for i in range(len(tiles)):
            if used[i]:
                continue

            used[i] = True
            self.helper(tiles, ans, cur + tiles[i], used)
            used[i] = False

    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        used = [False] * len(tiles)
        self.helper(tiles, ans, "", used)
        return len(ans)