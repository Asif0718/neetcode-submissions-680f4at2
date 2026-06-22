class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        numSet = set()
        longest = 0

        for r in range(len(s)):
            if s[r] not in numSet:
                numSet.add(s[r])
                longest = max(longest, r-l+1)
            else:
                while s[r] in numSet:
                    numSet.remove(s[l])
                    l+=1
                numSet.add(s[r])
                longest = max(r-l+1 , longest) 
        return longest                                                     
