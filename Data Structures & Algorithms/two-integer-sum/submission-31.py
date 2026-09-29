class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for it, val in enumerate(nums):
            d[val] = it
        
        for it, val in enumerate(nums):
            if target - val in d and d[target - val] != it:
                return [min(d[target - val], it), max(d[target - val], it)]
        
        
        