class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lis=[]
        l=0
        r=k
        sub_list=nums[:k]

        while r <= len(nums):
            max_num = max(sub_list)
            lis.append(max_num)
            l+=1
            r+=1
            sub_list=nums[l:r]    
        return lis    

