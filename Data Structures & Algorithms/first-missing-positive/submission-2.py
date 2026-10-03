class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = max(nums)
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for n in nums:
            hashmap[n] += 1
        m = 100
        for i in range(1,m):
            if i not in hashmap:
                return i
        

        
        


        
        
        