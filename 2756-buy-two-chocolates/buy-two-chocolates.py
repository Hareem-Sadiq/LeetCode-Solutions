class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices=sorted(prices)
        if money >=prices[0]+prices[1]:
            return(money-(prices[0]+prices[1]))
        else:
            return(money)