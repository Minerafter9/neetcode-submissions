class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        if s == "":
            return True
        while l < r:
            try:
                while not s[l].isalpha() and not s[l].isnumeric():
                    l += 1
                while not s[r].isalpha() and not s[r].isnumeric():
                    r -= 1
            except IndexError:
                return True
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

            
            



        