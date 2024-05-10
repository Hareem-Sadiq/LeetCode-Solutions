class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        prev_char = ord(s[0])  # Initialize with the ASCII value of the first character
        for i in range(1, len(s)):
            curr_char = ord(s[i])
            score += abs(curr_char - prev_char)
            prev_char = curr_char
        return score