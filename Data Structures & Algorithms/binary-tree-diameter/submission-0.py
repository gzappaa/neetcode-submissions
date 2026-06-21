# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        self.total_diameter = 0

        def height(root):
            if not root:
               return 0

            left = height(root.left)
            right = height(root.right)
            diameter = right + left

            self.total_diameter = max(self.total_diameter, diameter)
            return 1 + max(right, left)

        height(root)
        return self.total_diameter


        

        
        