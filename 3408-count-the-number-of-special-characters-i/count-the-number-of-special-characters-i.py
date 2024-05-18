class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        upper=[]
        lower=[]
        count=0
        for char in word:
            if char.isupper():
                upper.append(char)
            elif char.islower():
                lower.append(char)
        for u in set(upper):
            for l in set(lower):
                if ord(u.lower())==ord(l):
                    count+=1
                else:
                    continue
        return(count)