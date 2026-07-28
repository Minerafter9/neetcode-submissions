class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listnums = []
        for i in nums:
            if i in listnums:
                return True
            listnums.append(i)
        return False


        
        



