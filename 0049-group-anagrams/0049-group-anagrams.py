class Solution:
    def groupAnagrams(self, strs):
        seen = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in seen:
                seen[key] = []
            seen[key].append(word)
        return list(seen.values())


            


        
        