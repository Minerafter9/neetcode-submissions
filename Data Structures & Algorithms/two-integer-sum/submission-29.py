class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for it, val in enumerate(nums):
            store[val] = it
        for it, val in enumerate(nums):
            if target - val in store and it != store[target - val]:
                return [it, store[target - val]]
        