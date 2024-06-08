class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sumLeft = [0] * n
        sumRight = [0] * n
    
        for i in range(1, n):
            sumLeft[i] = sumLeft[i - 1] + nums[i - 1]
    
        for i in range(n - 2, -1, -1):
            sumRight[i] = sumRight[i + 1] + nums[i + 1]
    
        for i in range(n):
            if sumLeft[i] == sumRight[i]:
                return i

        return -1
        