import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        
        profit = 0
        
        for i in prices:
            minPrice = min(minPrice, i)
            profit = max(profit, i - minPrice)
        return profit
            
        
        