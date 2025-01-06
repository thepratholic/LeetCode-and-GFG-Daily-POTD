class Solution:
    def sumClosest(self, arr, target):
        # code here
        
        
        arr.sort()
        ans=float('inf')
        l=0
        n=len(arr)
        r=n-1
        a=[]
        while(l<r):
            if (arr[l]+arr[r])>target:
                if abs(target-arr[l]-arr[r])<ans:
                    ans=abs(target-arr[l]-arr[r])
                    a=[arr[l],arr[r]]
                    
                r=r-1
                
            else:
                
                if abs(target-arr[l]-arr[r])<ans:
                    ans=abs(target-arr[l]-arr[r])
                    a=[arr[l],arr[r]]
                l=l+1
        return a
