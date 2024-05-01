class Solution(object):
    def intToRoman(self, num):
        result = ""
        while num > 0:
            if num >= 1000:
                result = result + 'M'
                num = num - 1000
            elif num >= 900:
                result = result + 'CM'
                num = num - 900
            elif num >= 500:
                result = result + 'D'
                num = num - 500
            elif num >= 400:
                result = result + 'CD'
                num = num - 400
            elif num >= 100:
                result = result + 'C'
                num = num - 100
            elif num >= 90:
                result = result + 'XC'
                num = num - 90
            elif num >= 50:
                result= result + 'L'
                num = num - 50
            elif num >= 40:
                result = result + 'XL'
                num = num - 40
            elif num >= 10:
                result = result + 'X'
                num = num - 10
            elif num >= 9:
                result = result + 'IX'
                num = num - 9
            elif num >= 5:
                result = result + 'V'
                num = num - 5
            elif num >= 4:
                result = result +'IV'
                num = num - 4
            else:
                result = result + 'I'
                num = num - 1
        return result
    

        

        