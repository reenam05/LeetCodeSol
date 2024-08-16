class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = 0 
        c = 0
        if len(a) > len(b):
            diff = len(a) - len(b)
            c = b
        else:
            diff = len(b) - len(a)
            c = a
            
        for y in range(diff):
            c= str(0) + c
            
        if len(a) > len(b):
            b = c
        else:
            a = c

        count = 0 
        sum = []

        for x in range(len(a) - 1, -1,-1):
            if int(a[x]) + int(b[x]) + count == 2:
                sum.append(0)
                count+=1 
            elif int(a[x]) + int(b[x]) + count == 3:
                sum.append(1)
            elif int(a[x]) + int(b[x]) + count == 1:
                sum.append(1)
                count = 0
        sum.reverse()
        if count != 0:
            return(str(''.join(map(str, [1] + sum))))
        else:
            return(str(''.join(map(str, sum))))
                