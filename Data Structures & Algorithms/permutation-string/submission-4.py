class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        index = len(s1)
        l = 0
        for r in range(index-1,n+1):
            if sorted(s1) == sorted(s2[l:r+1]):
                return True
            else:
                l +=1
        return False
        