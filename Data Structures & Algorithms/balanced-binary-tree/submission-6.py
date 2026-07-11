# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = []
        ans = [True]
        self.height(root,ans)
        return ans[0]

    def height(self,node,ans):
        if node is None:
            return 0
        lh = self.height(node.left,ans)
        rh = self.height(node.right,ans)

        diff = abs(lh - rh)

        if diff >1:
            ans[0] = False

        return 1+max(lh,rh)






