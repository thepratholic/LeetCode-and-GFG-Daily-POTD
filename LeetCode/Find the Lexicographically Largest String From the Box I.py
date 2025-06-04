class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        maxi = ""
        m = n - numFriends + 1
        for i in range(n):
            maxi = max(maxi, word[i:i+m])
        return maxi