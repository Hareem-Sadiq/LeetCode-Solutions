class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr=0
        ans=0
        previous=0
        for i in range(len(nums)):
            if nums[i]==1:
                curr+=1
                if curr==len(nums):
                    return(len(nums)-1)
            else:
                ans=max(ans,previous+curr)
                previous=curr
                curr=0
        ans=max(ans,previous+curr)
        return(ans) 