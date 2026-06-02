class Solution(object):
    def romanToInt(self, s):
        v= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        for i in range(len(s)-1):
            if v[s[i]]>=v[s[i+1]]:
                total+=v[s[i]]
            else:
                total-=v[s[i]]
    
        return total+v[s[-1]]
        