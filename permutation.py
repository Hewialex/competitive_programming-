class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False

        s1_map = [0]*26
        s2_map = [0]*26

        for i in range( len(s1)) :
            s1_map[ ord(s1[i])-ord('a')] += 1
            s2_map[ ord(s2[i])-ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += 1 if s1_map[i]==s2_map[i] else 0

        left = 0
        for right in range( len(s1) , len(s2) ):
            if matches == 26 : return True  

            if s2[right] == s2[left] :
                left += 1
                continue

            index = ord(s2[right]) - ord('a')
            s2_map[index] += 1
            if s1_map[index] == s2_map[index] :
                matches += 1
            elif s1_map[index] + 1 == s2_map[index] :
                matches -= 1 

            index = ord(s2[left]) - ord('a')
            s2_map[index] -= 1
            if s1_map[index] == s2_map[index] :
                matches += 1
            elif s1_map[index] - 1 == s2_map[index] :
                matches -= 1  

            left += 1

        return matches == 26                 


