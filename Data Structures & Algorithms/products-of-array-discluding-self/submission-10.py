class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        store = 1
        out = []
        for i in nums:
            store = i*store
            prefix.append(store)
        store = 1
        for i in range(len(nums)):
            store = nums[-(i+1)]*store
            postfix.append(store)
        postfix = list(reversed(postfix))
        for i in range(len(nums)):
            if i == 0:
                out.append(postfix[1])
            elif i == len(nums) - 1:
                out.append(prefix[i - 1])
            else:
                out.append(prefix[i - 1]*postfix[i+1])
        return out
            
            