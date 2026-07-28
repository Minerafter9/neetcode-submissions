class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in set(nums):
            dictionary[i] = nums.count(i)
        tmp = 0
        tmp1 = 0
        list1 = []
        for i in range(k):
            tmp = 0
            for i in set(nums):
                if dictionary[i] > tmp:
                    tmp = dictionary[i]
                    tmp1 = i
            dictionary[tmp1] = -1
            list1.append(tmp1)
        return list1







            
        