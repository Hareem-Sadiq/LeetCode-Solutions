class Solution(object):
    def lengthOfLastWord(self, s):
        maximum=[]
        char=""
        s=s.lstrip()
        s=s.rstrip()
        if " " not in s:
            return(len(s))
        for i in range(len(s)-1,-1,-1):
            if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
                char=s[i]+char
            else:
                maximum.append(len(char))
                break
        
        return(max(maximum))