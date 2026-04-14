class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        max_price = 0

        for i in range(1,len(prices)):
            cost = prices[i]-mini
            max_price = max(max_price,cost)
            mini = min(mini,prices[i])

        return max_price    