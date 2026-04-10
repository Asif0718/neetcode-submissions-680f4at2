class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] +=1

        for r in range(len(s2)):
            s2_freq = [0] * 26
            winIdx = 0 
            idx = r

            while winIdx < len(s1) and idx < len(s2):
                s2_freq[ord(s2[idx]) - ord('a')] +=1
                idx+=1
                winIdx+=1

            if s1_freq == s2_freq:
                return True
        return False                         
