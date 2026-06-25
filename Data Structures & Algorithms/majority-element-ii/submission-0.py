class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val = defaultdict(int)
        res =[]

        for n in nums:
            val[n] += 1
        n = len(nums)
        s = n//3
        
        for (key,value) in val.items():
            if value > s:
                res.append(key)
        return res

        