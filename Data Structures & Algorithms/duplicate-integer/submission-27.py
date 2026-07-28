class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        num = 0
        for i in nums:
            if i in table:
                return True
            else:
                table[i] = 0
        return False