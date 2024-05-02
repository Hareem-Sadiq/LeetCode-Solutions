class Solution(object):
    def isStrictlyPalindromic(self, n):
        for base in range(2, n - 1):
            base_representation = ""
            quotient = n
            while quotient > 0:
                remainder = quotient % base
                base_representation = str(remainder) + base_representation
                quotient //= base
        if (base_representation==base_representation[-1:]):
            return True 
        return False
          

        