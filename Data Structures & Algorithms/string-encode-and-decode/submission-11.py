class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        if not strs:
            return chr(257)

        for it, val in enumerate(strs):
            if it != 0:
                str1 += "  "
            tmp = ""
            for j in val:
                tmp += chr(ord(j) + 5) 
            str1 += tmp
            
        
        return str1
        
        

    def decode(self, s: str) -> List[str]:
        if s and s[0] == chr(257):
            return []
        out = []
        for i in s.split("  "):
            tmp = ""
            for j in i:
                tmp += chr(ord(j) - 5)
            
            out.append(tmp)
        return out

