class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
    
        hex_chars = "0123456789abcdef"
        result = ""
        if num < 0:
            num += 2**32 
        
        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num //= 16
        
        return result
