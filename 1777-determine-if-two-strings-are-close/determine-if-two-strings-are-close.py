class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter
        
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False
 
        freq1 = Counter(word1)
        freq2 = Counter(word2)


        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True