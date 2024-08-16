class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr_len = len(nums)

        lo = 0
        hi = arr_len-1
        mid = 0

        while(lo <= hi):
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            elif hi - lo == 1 and nums[lo] < target and target < nums[arr_len-1]:
                return hi
            elif target < nums[mid]:
                hi = mid 
            elif target > nums[mid]:
                lo = mid + 1
                
        if nums[0] > target:
            return 0
        elif nums[arr_len-1] < target:
            return arr_len