class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        n=max(candies)
        for i in range(len(candies)):
            if (candies[i]+extraCandies>=n):
                result.append(True)
            else:
                result.append(False)
        return result
        