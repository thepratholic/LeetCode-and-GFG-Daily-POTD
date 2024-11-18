class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction.
    def reverse(self, arr, s, e):
        while s < e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
        return arr

    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)

        d %= n

        self.reverse(arr, 0, d - 1)
        self.reverse(arr, d, n - 1)
        self.reverse(arr, 0, n - 1)
        return arr