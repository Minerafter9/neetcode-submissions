class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = t.lower()
        s = s.lower()
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        if t == s:
            return True
        else:
            return False
        
        