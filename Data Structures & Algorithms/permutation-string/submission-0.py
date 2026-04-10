class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq=[0]*26
        

        for i in range(len(s1)):
            s1_freq[ord(s1[i])-ord('a')]+=1

        ws=len(s1)
        for i in range(len(s2)):
            s2_freq=[0]*26
            winIdx=0
            idx=i

            while winIdx < ws and idx < len(s2):
                s2_freq[ord(s2[idx])-ord('a')]+=1
                idx+=1
                winIdx+=1

            if s2_freq==s1_freq:
                return True
        return False        
