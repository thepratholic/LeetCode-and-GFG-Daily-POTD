class Solution:
    def countTriplets(self, arr, target):
        # code here
        
        count = 0
        n = len(arr)
        
        for i in range(n-2):
            
            j, k = i + 1, n - 1
            while j < k:
                sum_val = arr[i] + arr[j] + arr[k]
                
                if sum_val < target:
                    j += 1
                    
                elif sum_val > target:
                    k -= 1
                else:
                    count += 1
                    
                    tmp = j+1
                    while tmp < k and arr[tmp] == arr[tmp - 1]:
                        tmp += 1
                        count += 1
         
                    k -= 1
                        
        
        return count