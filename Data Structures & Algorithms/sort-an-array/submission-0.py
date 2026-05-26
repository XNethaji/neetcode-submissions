class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            j = i
            while nums[j-1] > nums [j] and j > 0:
                nums[j-1],nums[j] = nums[j], nums[j-1]
                j -=1
        return nums 
        