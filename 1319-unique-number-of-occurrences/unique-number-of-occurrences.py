class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count={}
        for i in arr:
            if i not in count:
                count[i]=arr.count(i)

        counts=set(count.values())
        if len(counts)==len(count.values()):
            return True
        else:
            return False

