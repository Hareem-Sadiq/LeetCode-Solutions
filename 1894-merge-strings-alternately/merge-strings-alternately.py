class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=""
        min_length_word=word2 if len(word2)<len(word1) else word1

        print(min_length_word)
        for i in range(len(min_length_word)):
            merged= merged + word1[i] + word2[i]

        if len(word1)==len(word2):
            return(merged)
        elif word1==min_length_word:
            merged= merged + word2[len(word1):]
            return(merged)
        else:
            merged= merged + word1[len(word2):]
            return(merged)
        
        