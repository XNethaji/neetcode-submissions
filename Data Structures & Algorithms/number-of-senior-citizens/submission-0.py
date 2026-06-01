class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            val = list(s)
            age = int("".join([val[11],val[12]]))
            if age > 60:
                count += 1
        return count

            
        
        