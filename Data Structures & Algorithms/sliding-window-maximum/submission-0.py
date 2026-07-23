class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        arr =[]

        while i < len(nums) - k + 1:
            index = nums[i:i+k]
            maxvalue = max(index)
            arr.append(maxvalue)
            
            i+=1
        return arr
        