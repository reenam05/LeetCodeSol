class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        for i, val in enumerate(nums):

            for j, val in enumerate(nums):
                if nums[i] == nums[j] and i != j:
                    tmp = nums[j]
                    
                    for k, val in enumerate(nums):
                        if k < length -1 and i <= k:
                            nums[k] = nums[k+1]
        
        k = 0
        for i, val in enumerate(nums):
            if i < length -1 and nums[i] != nums[i+1]:
                k = k + 1
        k = k + 1
        return k