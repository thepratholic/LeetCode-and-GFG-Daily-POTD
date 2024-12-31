class Solution:
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        arr.sort()
        longest = 1
        lastSmall = float('-inf')
        cnt = 0
        for i in range(len(arr)):
            if(arr[i]-1 == lastSmall):
                cnt += 1
                lastSmall = arr[i]
            elif(lastSmall != arr[i]):
                cnt = 1
                lastSmall = arr[i]
            longest = max(longest, cnt)
        return longest