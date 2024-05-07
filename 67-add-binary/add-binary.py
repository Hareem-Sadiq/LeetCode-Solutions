class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        binary_sum = lambda a,b : bin(int(a, 2) + int(b, 2))
        return(str(binary_sum(a,b)[2:]))