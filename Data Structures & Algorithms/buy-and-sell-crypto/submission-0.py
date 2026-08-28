class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        r=l+1
        profit=0
        max_profit=0
        for r in range(1,n):
            if prices[l]>=prices[r]:
                l=r
            else:
                profit = prices[r] - prices[l]
            max_profit = max(profit,max_profit)

        return max_profit
            
        