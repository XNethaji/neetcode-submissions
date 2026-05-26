class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT={}
        countS ={}
        n = len(s)
        if len(s) != len(t):
            return False

        for i in range(n):
            countT[t[i]] = 1 + countT.get(t[i],0)
            countS[s[i]] = 1 + countS.get(s[i],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
        