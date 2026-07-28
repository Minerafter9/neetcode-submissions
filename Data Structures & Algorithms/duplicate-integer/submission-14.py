class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listnums = {}
        for i in nums:
            if i in listnums:
                return True
            listnums[i] = 1
        return False


        
        



