class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1,1]

        if n == 1 or n == 0 :
            return(1)

        for i in range(1,n,1):
            arr.append(arr[-1] + arr[-2])
            
        return arr[n]