# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def backtrack(node1, node2):

            
            
            if node1 == None and node2 == None:
                return True
            elif node1 == None or node2 == None: 
                return False
            else:
                if node1.val != node2.val: return False
                if not backtrack(node1.left, node2.right): return False
                if not backtrack(node2.left, node1.right): return False
                return True

                
        return backtrack(root, root)

        # def search(left, right):
        #     if left is None and right is None:
        #         return True
        #     if left is None or right is None:
        #         return False
        #     return left.val == right.val and search(left.left, right.right) and search(left.right, right.left)
        # return search(root, root)
