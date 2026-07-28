class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1, table2 = {}, {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            table1[s[i]] = 1 + table1.get(s[i], 0)
            table2[t[i]] = 1 + table2.get(t[i], 0)
            
        if table1 == table2:
            return True
        else:
            return False
        