class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha1 = {}
        alpha2 = {}

        if len(s) != len(t):
            return False
        for i in s:
            if i in alpha1:
                alpha1[i] += 1
            else:
                alpha1[i] = 1
        for i in t:
            if i in alpha2:
                alpha2[i] += 1
            else:
                alpha2[i] = 1 
        if alpha1 == alpha2:
            return True
        else:
            return False
        