class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        prev_seq = self.countAndSay(n-1)
        result = ""
        count = 1
        for i in range(len(prev_seq)):
            if i + 1 < len(prev_seq) and prev_seq[i] == prev_seq[i+1]:
                count += 1
            else:
                result += str(count) + prev_seq[i]
                count = 1
        return result


            