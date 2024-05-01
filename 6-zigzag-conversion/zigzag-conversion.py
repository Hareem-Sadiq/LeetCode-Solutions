class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lst=[]
        if numRows==1:
            return(s)
        for r in range(numRows):
            inc=2*(numRows-1)
            for i in range(r,len(s),inc):
                lst.append(s[i])
                if r>0 and r<(numRows-1)and i+inc-2*r<len(s):
                    lst.append(s[i+inc-2*r])

        delimiter=''
        string=delimiter.join(lst)
        return(string)
