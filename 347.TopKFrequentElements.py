class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_dict = {}

        for val in nums:
            if val in my_dict:
                my_dict[val] = my_dict[val] + 1
            else:
                my_dict[val] = 1

        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
        arr = []

        for key in sorted_dict:
            arr.append(sorted_dict[key])
        
        arr_len = len(arr)
        return(arr[arr_len - k:])