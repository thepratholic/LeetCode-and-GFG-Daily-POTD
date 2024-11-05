class Solution:
    def treePathSum(self,root):
        def dfs(node, current_number):
            if not node:
                return 0

            current_number = current_number * 10 + node.data

            if not node.left and not node.right:
                return current_number

            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)

            return left_sum + right_sum

        return dfs(root, 0)