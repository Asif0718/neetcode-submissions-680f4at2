class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        max_profit=0

        for i in range(1,len(prices)):
            cost=prices[i]-mini
            max_profit=max(max_profit,cost)
            mini=min(mini,prices[i])
        return max_profit