class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=0
        st=''
        for i in s:
            while j < len(t):
                if t[j]==i:
                    st=st+t[j]
                    j=j+1
                    break
                else:
                    j=j+1


        if s==st:
            return True
        else:
            return False
