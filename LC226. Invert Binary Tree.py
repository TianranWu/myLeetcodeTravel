# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:

#         def backtrack(node):
            
#             if node.right == None:
#                 backtrack(node.left)
#                 node.right = node.left
#                 node.left = None
#             elif node.left  == None:
#                 backtrack(node.right)
#                 node.left = node.right
#                 node.right = None
#             else:
#                 backtrack(node.left)
#                 backtrack(node.right)
#                 temp = node.left
#                 node.left = node.right
#                 node.right = temp
            
#         if root == None:
#             pass        
#         else:
#             backtrack(root)

#         return root
    
    
    class Solution:
        def invertTree(self, root: TreeNode) -> TreeNode:

            def backtrack(node):
            
            if node == None:
                pass
            else:
                backtrack(node.left)
                backtrack(node.right)
                node.left, node.right = node.right, node.left
                
            backtrack(root)

            return root
