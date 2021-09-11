# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    # Recursion
    
        res = []
        def backtrack(node):
            if node == None:
                pass
            else:
                backtrack(node.left)
                res.append(node.val)
                backtrack(node.right)
        
        backtrack(root)

        return res
