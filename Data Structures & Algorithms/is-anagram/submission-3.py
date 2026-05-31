class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1= {}
        count2 = {}

        if len(s) == len(t):
            for i in range(len(s)):
                count1[s[i]] = 1+count1.get(s[i],0)
                count2[t[i]] = 1+count2.get(t[i],0)

            if count1 == count2:
                return True
            else:
                return False        
        else:
            return False    