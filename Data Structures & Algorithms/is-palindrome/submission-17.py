class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        if s == "":
            return True
        while l < r:
            while l < r and not isnumal(s[l]):
                l += 1   
            while l < r and not isnumal(s[r]):
                r -= 1
            
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

## only works for lower and nums
def isnumal(char):
    return (ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9"))
    

            
            



        