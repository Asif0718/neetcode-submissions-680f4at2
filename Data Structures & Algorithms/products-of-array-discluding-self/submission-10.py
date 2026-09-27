class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        pre = 1

        for i in range(len(nums)):
            res[i] = pre
            pre = pre * nums[i]

        post = 1
        ans = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            ans[i] = post 
            post = post*nums[i]

        for i in range(len(nums)):
            res[i] *= ans[i]

        return res            