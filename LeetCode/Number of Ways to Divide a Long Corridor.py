class Solution:
    def numberOfWays(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        if s.count('S') % 2 != 0 or s.count('S') == 0:
            return 0
        if s.count('S') == 2:
            return 1

        pref = [0] * n
        pref[0] = 1 if s[0] == 'S' else 0

        for i in range(1, n):
            pref[i] = pref[i - 1] + (s[i] == 'S')

        ans = 1
        i = 0

        while i < n:
            if pref[i] % 2 == 0 and pref[i] >= 2:
                j = i + 1
                plants = 0

                while j < n and s[j] == 'P':
                    plants += 1
                    j += 1

                if j < n: 
                    ans = (ans * (plants + 1)) % MOD

                i = j
            else:
                i += 1

        return ans
