class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []

        def dfs(i):
            if i >= len(nums):
                res.append(subSet[:])
                return

            #left tree to add nums[i]
            subSet.append(nums[i])
            dfs(i+1)

            subSet.pop()
            dfs(i+1)

        dfs(0)
        return res        