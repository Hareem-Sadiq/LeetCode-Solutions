class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums=list(set(nums))
        if len(nums)<3:
            return(max(nums))
        nums.sort()
        return(nums[-3])