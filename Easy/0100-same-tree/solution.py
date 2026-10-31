# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        result = []
        def preorder(root1,root2):
            if not root1 and not root2:
                return 
            if not root1 or not root2:
                result.append(False)
                return 
            
            result.append(root1.val == root2.val)
            preorder(root1.left,root2.left)  
            preorder(root1.right,root2.right)

        preorder(p,q)
        if False in result:
            return False
        else:
            return True
              
