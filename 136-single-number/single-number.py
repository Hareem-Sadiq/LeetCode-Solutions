import numpy as np
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_arr = np.array(nums)
        unique_elements, counts = np.unique(num_arr, return_counts=True)
        return(int(unique_elements[counts == 1]))