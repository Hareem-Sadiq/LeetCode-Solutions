class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumLeft=0
        total_sum=sum(nums)
        for i in range(len(nums)):
            sumRight=total_sum -nums[i]-sumLeft
            if sumRight==sumLeft:
                return i
            sumLeft+=nums[i]
        return -1
        