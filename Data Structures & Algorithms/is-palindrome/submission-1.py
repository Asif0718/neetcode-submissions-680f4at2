class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns_1=''
        for i in range(len(s)):
            if (ord(s[i])>=65 and ord(s[i])<=122) or (ord(s[i])>=48 and (ord(s[i])<=57)):
                ns_1+=s[i]
            
            else:
                continue
        ns=ns_1.lower()
        ns_2=''
        for i in range(len(ns)-1,-1,-1):
            ns_2+=ns[i]
         
        return ns==ns_2      

