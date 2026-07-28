class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for it, num in enumerate(numbers):
            target1 = target - num
            l, r = 0, len(numbers) - 1

            while l <= r:
                m = l + (r - l) // 2

                if target1 > numbers[m]:
                    l = m + 1
                elif target1 < numbers[m]:
                    r = m - 1
                else:
                    if it != m:
                        return [it + 1, m + 1]
                    else:
                        return [it + 1, m + 2]
                    

        