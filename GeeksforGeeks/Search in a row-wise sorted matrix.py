class Solution:

    def searchRowMatrix(self, mat, x):
        def binary_search(row, target):
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        for row in mat:
            if binary_search(row, x):
                return True
        return False