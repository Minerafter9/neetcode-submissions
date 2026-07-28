class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        if s == "":
            return True
        while l < r:
            
            while not isnumal(s[l]):
                if l < len(s) - 1:
                    l += 1
                else:
                    break
            while not isnumal(s[r]):
                if r > -1:
                    r -= 1
                else:
                    break
            
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

## only works for lower and nums
def isnumal(char):
    return (ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9"))
    

            
            



        