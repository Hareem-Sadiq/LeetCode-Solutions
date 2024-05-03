class Solution(object):
    def removeDuplicates(self, nums):
        index = 0
        for num in nums:
            # If the current number is the same as the previous two numbers,
            # skip it to maintain at most two duplicates
            if index < 2 or num > nums[index - 2]:
                nums[index] = num
                index += 1

        return index
        