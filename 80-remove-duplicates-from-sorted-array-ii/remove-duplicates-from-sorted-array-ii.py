class Solution(object):
    def removeDuplicates(self, nums):
        index = 0
        for num in nums:
            if index < 2:
                index += 1
            elif (num > nums[index - 2]):
                nums[index] = num
                index+=1
    

        return index
        