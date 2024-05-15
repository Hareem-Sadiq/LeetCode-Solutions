class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        len_char=len(word)
        count=0
        index=None
        for char in word:
            if ord(char)>=65 and ord(char)<=90:
                count+=1
                if char==word[0]:
                    index=True
                continue
        if (count==0)or (count==len_char) or (index and count==1):
            return(True)
        else:
            return(False)