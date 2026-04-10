class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        if not root:
            return ans
        q = deque()
        q.append(root)    

        while len(q):
            length = len(q)
        
            for i in range(length):
                curr = q.popleft()
                temp = curr.val 
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(temp)
        return ans