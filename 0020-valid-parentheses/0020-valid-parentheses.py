class Solution:
    def isValid(self, s: str) -> bool:
        pairs={')':'(',']':'[','}':'{'}
        stack=[]
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if pairs[ch]==stack[-1]:
                    stack.pop()
                else:
                    return False
                    

        return not stack