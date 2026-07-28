class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        try:
            table = {}
            hash1 = {}
            if len(s) != len(t):
                return False
            for i in s:
                if i not in table:
                    table[i] = 1
                else:
                    table[i] += 1
            for i in t:
                if i not in hash1:
                    hash1[i] = 1
                else:
                    hash1[i] += 1 
            for i in s:
                if table[i] != hash1[i]:
                    return False
            return True
        except KeyError:
            return False
