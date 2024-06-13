# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=1,n
        while True: 
            mid=(l+r)//2
            result=guess(mid)
            if result > 0:
                l,r=mid+1,r
            elif result < 0:
                l,r= l,mid-1
            else:
                return mid 
