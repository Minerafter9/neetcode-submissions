class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s.lower()), list(t.lower())
        s.sort(), t.sort()
        if t == s:
            return True
        else:
            return False
        
        