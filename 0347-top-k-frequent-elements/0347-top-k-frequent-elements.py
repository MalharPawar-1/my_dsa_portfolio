class Solution(object):
    def topKFrequent(self, nums, k):
        fq={}
        for i in nums:
            fq[i]=fq.get(i,0)+1
        return sorted(fq,key=fq.get, reverse=True)[:k]    
        