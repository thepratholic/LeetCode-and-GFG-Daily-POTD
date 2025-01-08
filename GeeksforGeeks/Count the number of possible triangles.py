class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        cnt = 0
        
        n = len(arr)
        
        for i in range(n-1, -1, -1):
            s, e = 0, i-1

            while s < e:
                if(arr[s] + arr[e] > arr[i]):
                    cnt += e-s
                    e -= 1

                else:
                    s += 1

        return cnt