class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        length = len(digits)

        for x in digits:
            num = str(num) + str(x)
            
        num = int(num)
        num +=1

        expo = length 
        new_arr = []
        i = 0

        for x in range(length + 1):
            y = num // 10**expo
            if num - 10**expo * y >= 0:
                num = num - 10**expo * y
            expo -=1
            new_arr.append(y)
            
        if new_arr[0] == 0:
            new_arr.remove(0)
            
        return(new_arr)