class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number = {}
        for i , num in enumerate(nums):
            k = target - num
            if k not in number:
                number[num] = i
            else:
                return [number[k],i]
        
        
    

        
            



        
        


        