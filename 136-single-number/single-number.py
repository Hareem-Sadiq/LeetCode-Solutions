class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            duplicate=nums.count(num)
            if (duplicate==1):
                return (num)
            