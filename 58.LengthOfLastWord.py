class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        i = 0

        for letter in s:
            if letter != ' ':
                i+=1
            elif letter == ' ' and i != 0:
                arr.append(i)
                i = 0

        if i != 0:
            arr.append(i)
            
        return(arr[-1])