class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ones=[]
        for i in range(0,n+1):
            binary=bin(i)
            ones.append(str(binary).count('1'))
        return(ones)

