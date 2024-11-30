
class Solution:
    def areAnagrams(self, s1, s2):
        #code here
        visited = [0] * 26

        if len(s1) != len(s2): return False

        for i in range(len(s1)):
            visited[ord(s1[i]) - ord("a")] += 1
            visited[ord(s2[i]) - ord("a")] -= 1

        for x in visited:
            if x != 0: return False

        return True