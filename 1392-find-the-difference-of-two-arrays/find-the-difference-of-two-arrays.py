class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer=[]
        nums1=set(nums1)
        nums2=set(nums2)
        nums1_copy = set(nums1)
        nums2_copy = set(nums2)

        for n1 in nums1_copy:
            if n1 in nums2_copy:
                nums1.remove(n1)
        answer.append(nums1)

        for n2 in nums2_copy:
            if n2 in nums1_copy:
                nums2.remove(n2)
        answer.append(nums2)
        
        return answer



        