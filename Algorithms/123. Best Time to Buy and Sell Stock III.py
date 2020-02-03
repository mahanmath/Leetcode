class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = len(prices)
        if(L == 0): return 0
        
        min_forward = [0] * L
        max_profit_forward = [0] * L
        min_forward[0] = prices[0]
        
        max_backward = [0] * L
        max_backward[-1] = prices[-1]
        max_profit_backward = [0] * L
        
        for i in range(1, L):
            #Forward Profit
            min_forward[i] = min([min_forward[i - 1], prices[i]])
            profit_now = prices[i] - min_forward[i]
            max_profit_forward[i] = max([max_profit_forward[i-1], profit_now])
            
            #Backward Profit
            max_backward[L - i - 1] = max([max_backward[L - i], prices[L - i - 1]])
            profit_now = max_backward[L - i - 1] - prices[L - i - 1]  
            max_profit_backward[L - i - 1] = max([max_profit_backward[L -i], profit_now])
        
        return max([max_profit_backward[i] + max_profit_forward[i] for i in range(L)])
            