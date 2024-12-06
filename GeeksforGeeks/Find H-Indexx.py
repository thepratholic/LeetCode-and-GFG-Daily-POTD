class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        citations.sort(reverse=True)
        hInd = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                hInd = i + 1
            else: break

        return hInd