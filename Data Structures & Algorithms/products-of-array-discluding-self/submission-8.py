class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix

        ans = [1] * len(nums)
        postfix = 1 

        for i in range(len(nums)-1,-1,-1):
            ans[i] = postfix 
            postfix = postfix * nums[i]

        for i in range(len(nums)):
            res[i] = res[i]*ans[i]
        return res                