class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for x in s:
            if x == '{':
                for x in s:
                    if x == '}':
                        return True
            if x == '(':
                for x in s:
                    if x ==')':
                        return True
            if x =='[':
                for x in s:
                    if x ==']':
                        return True