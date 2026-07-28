class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target < matrix[m][0]:
                r -= 1
            elif target > matrix[m][0]:
                l += 1
            else:
                return True
        row = l - 1
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target < matrix[row][m]:
                r -= 1
            elif target > matrix[row][m]:
                l += 1
            else:
                return True
        return False
        