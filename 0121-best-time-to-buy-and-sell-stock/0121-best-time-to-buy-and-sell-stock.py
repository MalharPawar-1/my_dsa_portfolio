class Solution(object):
    def maxProfit(self, prices):
        mn=prices[0]
        prof=0
        for p in prices:
            mn = min(mn,p)
            prof=max(prof,p-mn)
        return prof
        
        