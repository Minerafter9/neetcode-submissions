class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in table:
                return [table[tmp], i]
            else:
                table[nums[i]] = i