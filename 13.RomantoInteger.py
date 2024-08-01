class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

        book = {'I': I, 'V': V, 'X':X, 'L':L, 'C':C, 'D': D, 'M': M}

        length = len(s)
        count = 0

        for x in range(length-1):
            if book[s[x]] >= book[s[x+1]]:
                count = count + book[s[x]]
            elif book[s[x]] < book[s[x+1]]:
                count = count - book[s[x]]
                
        count = count + book[s[length-1]]
        return count
        