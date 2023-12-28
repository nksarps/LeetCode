# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        # Check if the current nodes have the same value
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# link, https://leetcode.com/problems/same-tree/