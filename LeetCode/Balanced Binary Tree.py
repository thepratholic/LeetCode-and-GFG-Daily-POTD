# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def f(root):
            if not root:
                return 0

            lh = f(root.left)
            rh = f(root.right)

            if abs(lh - rh) > 1 or lh == -1 or rh == -1:
                return -1

            return max(lh, rh) + 1


        return f(root) != -1