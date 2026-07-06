class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l , r = 0 , len(nums)-1
        n= len(nums)
        while l <= r :
            mid = (l+r)//2

            if nums[mid] < nums[(mid-1+n)%n] and nums[mid] < nums[(mid+1)%n]:  # situation like [4,5,1,2,3] => 1<5 and 1 <2  5>1<2
                return nums[mid]
            elif nums[mid] > nums[r]: # [4,5,1,2,3]  here mid = 5 and 5 > nums[r] search search right side
                l = mid +1
            else:                #[11,13,15,17] mid = 13 and 13 < nums[r] so search left side 
                r = mid - 1 
        return nums[0]                

#https://youtu.be/5yq2PAKonho?si=rDpNLT3XZXY_tn_0