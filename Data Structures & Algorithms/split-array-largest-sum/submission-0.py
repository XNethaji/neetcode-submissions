class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(largest):
            cursum = 0
            array = 1

            for num in nums:
                cursum += num
                if cursum > largest:
                    array+= 1
                    if array > k:
                        return False
                    cursum = num 
            return True 
        
        l , r = max(nums) , sum(nums)
        res = r
        while l <= r:
            mid = l + ((r-l)// 2)
            if cansplit(mid):
                res = mid
                r = mid -1
            else :
                l = mid+ 1
        return res 
                


        
        