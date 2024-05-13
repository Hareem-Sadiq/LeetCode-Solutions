class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        # Reverse the order of words
        words.reverse()
        # Join the words back together with a single space
        return ' '.join(words)