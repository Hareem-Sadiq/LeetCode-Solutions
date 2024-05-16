class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        v=0
        consonant=0
        vowels=['a','e','i','o','u'] 
        if len(word)>=3 and word.isalnum():
            for char in word.lower():
                if char in vowels:
                    v+=1
                elif (ord(char)>=97 and ord(char)<=122):
                    consonant+=1
        else:
            return(False)

        if (consonant>=1 and v>=1):
            return (True)
        else:
            return (False)

                
                
            