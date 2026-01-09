# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
from collections import deque
from typing import Optional


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        max_depth = 0
        def bfs(node):
            nonlocal max_depth
            q = deque()
            q.append((node, 0))

            while q:
                cur, depth = q.popleft()
                max_depth = max(max_depth, depth)

                if cur.left:
                    q.append((cur.left, depth + 1))

                if cur.right:
                    q.append((cur.right, depth + 1))

        bfs(root)

        def dfs(node, cur_depth):

            if not node:
                return None

            if cur_depth == max_depth:
                return node 

            left = dfs(node.left, cur_depth + 1)
            right = dfs(node.right, cur_depth + 1)

            if left and right:
                return node

            return left if left else right

        return dfs(root, 0)