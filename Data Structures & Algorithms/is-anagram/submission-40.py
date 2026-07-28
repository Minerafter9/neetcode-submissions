class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        s.sort(), t.sort()
        if t == s:
            return True
        else:
            return False
        
        