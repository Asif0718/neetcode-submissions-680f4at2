# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def helper(self, root, min_node, max_node):
        if root is None:
            return True

        
        #for left side of Node condition
        if max_node is not None and root.val >= max_node.val:
            return False

        #for right side of node condition
        if min_node is not None and root.val <= min_node.val:
            return False    

        return (self.helper(root.left, min_node, root) and
                self.helper(root.right, root, max_node))



     def isValidBST(self,root): 
         return self.helper(root,None,None)             