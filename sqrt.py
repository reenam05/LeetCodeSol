class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 1

        while 1 == 1:
            if a * a  == x:
                return a
            elif a * a > x:
                return a -1
            a+=1