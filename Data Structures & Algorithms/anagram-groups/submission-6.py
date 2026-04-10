class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1

            key = tuple(count)
            if key in result:
                result[key].append(word)
            else:
                result[key]=[word]    
        return list(result.values())              