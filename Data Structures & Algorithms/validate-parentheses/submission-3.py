class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = { "(":")", "{":"}", "[":"]"}

        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            elif i in valid:
                stack.append(valid[i])
            else:
                return False     
        if stack:
            return False         
        return True