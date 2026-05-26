class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number = {}
        n = len(nums)
        for i , num in enumerate (nums):
            k = target - num
            if k in number:
                return[number[k] , i]
            number[num] = i
            

        
            



        
        


        