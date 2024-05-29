class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(num1, num2):
            while num2:
                num1, num2 = num2, num1 % num2
            return (num1)

        def check(s1,s2):
            return (s1== s2 * (len(s1) // len(s2)))
    
        len_gcd = gcd(len(str1), len(str2))
        candidate = str1[:len_gcd]
    
        if check(str1, candidate) and check(str2, candidate):
            return candidate
        else:
            return ""