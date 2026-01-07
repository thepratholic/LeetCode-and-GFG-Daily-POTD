# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = (10 ** 9) + 7
        ans = 0

        def total(node):
            if not node:
                return 0

            cur = node.val
            left = total(node.left)
            right = total(node.right)

            return cur + left + right

        
        totalSum = total(root)

        def f(node):
            nonlocal ans

            if not node:
                return 0

            left = f(node.left)
            right = f(node.right)

            sub_tree_sum = node.val + left + right

            ans = max(ans, sub_tree_sum * (totalSum - sub_tree_sum))
            
            return sub_tree_sum

        f(root)
        return ans % MOD