class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        count2={}
        if len(s)==len(t):
            for i in range(len(s)):
                count[s[i]]=1+count.get(s[i],0)
                count2[t[i]]=1+count2.get(t[i],0)
            return count==count2 
        else:
            return False    