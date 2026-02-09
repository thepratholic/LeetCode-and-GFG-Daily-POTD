# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)

        inorder(root)

        def f(l, r):
            if l > r:
                return None

            mid = (l + r) >> 1
            new_node = TreeNode(vals[mid])
            new_node.left = f(l, mid - 1)
            new_node.right = f(mid + 1, r)
            return new_node

        return f(0, len(vals) - 1)