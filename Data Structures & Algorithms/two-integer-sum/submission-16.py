class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in nums:
                for j in range(len(nums)):
                    if nums[j] == tmp and j != i:
                        return [i, j]
                        