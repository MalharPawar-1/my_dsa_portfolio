class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)
        
        