class Solution:

    def kthElement(self, nums1, nums2, k):
        n, m, i, j, tmp = len(nums1), len(nums2), 0, 0, []
        while (i < n and j < m):
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i+=1
            else:
                tmp.append(nums2[j])
                j+=1
            
        while(i < n):
            tmp.append(nums1[i])
            i+=1
        while(j < m):
            tmp.append(nums2[j])
            j+=1
        
        for index in range(len(tmp)):
            if (index == k-1):
                return tmp[index]