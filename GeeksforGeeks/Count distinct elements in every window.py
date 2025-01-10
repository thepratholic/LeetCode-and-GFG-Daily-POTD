class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        ans = []
        freq_map = {}
        distinct_count = 0
        
        # Initialize the frequency map for the first window
        for i in range(k):
            if arr[i] not in freq_map:
                freq_map[arr[i]] = 0
                distinct_count += 1
            freq_map[arr[i]] += 1
        
        ans.append(distinct_count)
        
        # Slide the window
        for i in range(k, n):
            # Remove the element going out of the window
            if freq_map[arr[i - k]] == 1:
                distinct_count -= 1
                del freq_map[arr[i - k]]
            else:
                freq_map[arr[i - k]] -= 1
            
            # Add the new element coming into the window
            if arr[i] not in freq_map:
                freq_map[arr[i]] = 0
                distinct_count += 1
            freq_map[arr[i]] += 1
            
            ans.append(distinct_count)
        
        return ans
