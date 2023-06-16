class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        l=0
        r=1
        while r<len(prices):
            curr_price=prices[r]-prices[l]
            if prices[r]>prices[l]:
                max_profit=max(max_profit,curr_price)
            else:
                l=r
            r=r+1
        return max_profit