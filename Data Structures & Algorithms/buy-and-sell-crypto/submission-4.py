class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxProfit = 0

        for i in range(1,len(prices)):
            cost = prices[i] - mini
            maxProfit = max(cost , maxProfit)
            mini = min(prices[i] , mini)
        return maxProfit    