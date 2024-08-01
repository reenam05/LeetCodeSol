class Solution(object):
    def twoSum(self, nums, target):
        
        my_dict = {}

        for index, value in enumerate(nums):
            my_dict[index] = value
            for i,x in enumerate(my_dict.values()):
                if(x == target - my_dict[index] and i != index):
                    return [i,index]