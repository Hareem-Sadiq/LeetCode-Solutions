class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumLeft=0
        sumRight=[0]*len(nums)
        total_sum=sum(nums)
        for i in range(len(nums)):
            sumRight[i]=total_sum -nums[i]-sumLeft
            if sumRight[i]==sumLeft:
                return i
            sumLeft+=nums[i]
        return -1
        