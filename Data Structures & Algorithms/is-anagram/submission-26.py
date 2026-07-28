class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        print(s)
        print(t)
        s.sort()
        t.sort()
        if s == t:
            return True
        else:
            return False