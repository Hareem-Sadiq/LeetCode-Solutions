class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        count_dict=Counter(nums)
        count=0
        for num in list(count_dict.keys()):
            diff=k-num
            if diff==num:
                count+=count_dict[num]//2
            else:
                count+=min(count_dict[num],count_dict[diff])
                del count_dict[num]
                del count_dict[diff]
        return count
        
