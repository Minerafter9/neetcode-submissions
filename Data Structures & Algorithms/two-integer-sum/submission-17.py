class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        number = 0
        for i in nums:
            table[i] = number
            number += 1
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in table:
                for j in range(len(nums)):
                    if nums[j] == tmp and j != i:
                        return [i, j]
                        