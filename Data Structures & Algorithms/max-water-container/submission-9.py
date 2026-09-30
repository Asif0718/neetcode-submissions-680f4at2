class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0,len(heights)-1

        maxCapacity = 0

        while l <= r:
            lh = heights[l]
            rh = heights[r]

            area = (r-l) * min(lh,rh)
            maxCapacity = max(maxCapacity,area)

            if lh < rh :
                l+=1
            elif rh < lh:
                r-=1
            else:
                l+=1
        return maxCapacity
                        