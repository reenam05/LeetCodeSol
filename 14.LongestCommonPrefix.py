class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = 0
        for string in strs:
            if len(string) < length:
                length = len(string)

        strs.sort()
        
        output = ""
        for i in range(4):
            word_one = strs[0]
            word_last = strs[-1]

            if word_one[i] == word_last[i]:      
                output = output + word_one[i]
            else:
                break
        
        return output
        