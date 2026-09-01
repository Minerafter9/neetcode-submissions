class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = nums[0]
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                low = min(low, nums[l])
                break
            m = l + (r - l) // 2
            
            if nums[l] <= nums[m]:
                l = m + 1
                low = min(low, nums[l], nums[m])
            elif nums[m] <= nums[r]:
                r = m - 1
                low = min(low, nums[r], nums[m])
            else:
                return -1
        return low

        