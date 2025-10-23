class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        tmp = s
        while len(tmp) > 2:
            ans = []
            for i in range(len(tmp) - 1):
                first = int(tmp[i])
                second = int(tmp[i + 1])

                ans.append((first + second) % 10)

            tmp = "".join(str(x) for x in ans)

        return tmp[0] == tmp[-1]