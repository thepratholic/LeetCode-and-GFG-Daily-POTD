class Solution:
    def canServe(self, arr):
        
        n = len(arr)
        
        five = 0
        ten = 0
        
        for i in range(n):
            if arr[i] == 5:
                five += 1
                
            elif arr[i] == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                    
                else: return False
                
            else:
                # customer has 20 rs
                if (five >= 1 and ten >= 1):
                    five -= 1
                    ten -= 1
                    
                elif five >= 3:
                    five -= 3
                else:
                    return False
                        
        return True
        