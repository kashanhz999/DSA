class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_ = (str)(x)
        str2  = str_[::-1]
        
        if str_ == str2:
            return True
        else:
            return False
        
        