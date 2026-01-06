# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
from collections import defaultdict
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        mpp = defaultdict(list)
        
        def f(node, level):
            if not node:
                return

            mpp[level].append(node.val)

            f(node.left, level + 1)
            f(node.right, level + 1)

        f(root, 1)

        maxi = float('-inf')
        ans = 1

        for k, v in mpp.items():
            s = sum(v)     
            if s > maxi:
                maxi = s
                ans = k

        return ans
