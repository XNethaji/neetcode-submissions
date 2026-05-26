class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        l = len(nums)

        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
            if hashmap[n] > l//2:
                return n


        