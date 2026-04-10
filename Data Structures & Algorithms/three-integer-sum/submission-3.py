class Solution:
    def threeSum(self, nums) :
        res = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] +nums[j]+nums[k] == 0:
                        num = [nums[i],nums[j],nums[k]]
                        res.add(tuple(num))
        return [list(i) for i in res]          