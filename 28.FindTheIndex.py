class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_length = len(needle)
        
        if needle in haystack:
            needle_i = 0
            haystack_i = 0
            for x in haystack:
                haystack_i+=1
                if needle[needle_i] == x:
                    if needle_i == needle_length - 1:
                        return(haystack_i - needle_length)
                        break
                    needle_i+=1
                    
        return -1