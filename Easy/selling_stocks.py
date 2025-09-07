class Solution(object): 
    def maxProfit(self, prices): 
        profit = 0
        left = 0 
        n = len(prices)

        for right in range(1, n):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
        return(profit)
    
solution = Solution()

print(solution.maxProfit([1,2,4,2,5,7,2,4,9,0,9]))