class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        nums = sorted(num)
        n = len(nums)

        mid = n // 2

        if n % 2 == 0:
            m = (nums[mid] + nums[mid - 1]) / 2
            return m
        else:
            return nums[mid]
            

        



    
        