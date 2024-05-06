import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if '*'*3 in p and s not in p:
            return False
        elif '*'*3 in p and s in p:
            return True
        a=re.match(p,s)
        if a is None:
            return(False)
        if a.group(0)==s:
            return(True)
