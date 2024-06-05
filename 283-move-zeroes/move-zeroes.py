class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        j=0
        for i in nums:
            if i!=0:
                nums[j]=i
                j=j+1

        while j!=len(nums):
            nums[j]=0
            j=j+1
            
            
