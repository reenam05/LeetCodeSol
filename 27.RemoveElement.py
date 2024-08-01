class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in nums:
            if i != val:
                k+=1

        j = 0
        for i in range (0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        
        return k