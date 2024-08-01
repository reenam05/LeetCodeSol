class Solution(object):
    def isPalindrome(self, x):
        
        strx = str(x)
        charx = list(strx)
        diffx = list(strx)
        length = len(strx)

        for i, c in enumerate(charx):
            charx[i] = diffx[length - 1]
            length = length - 1
        
        new_str = ''.join(charx)

        if new_str == strx:
            return True
        else:
            return False