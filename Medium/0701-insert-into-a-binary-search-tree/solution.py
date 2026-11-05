# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return TreeNode(key)

        if root.val < key:
            root.right = self.insertIntoBST(root.right,key)
        if root.val > key:
            root.left = self.insertIntoBST(root.left,key)

        return root

    
