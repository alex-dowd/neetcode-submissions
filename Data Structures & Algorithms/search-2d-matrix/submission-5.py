class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        temp = True
        if len(matrix) == 1:
            for num in matrix[0]:
                if num == target:
                    return True
            return False
        while temp:
            if target >= matrix[row][0] and target < matrix[row + 1][0]:
                for num in matrix[row]:
                    if num == target:
                        return True                   
                return False
            else:
                row += 1
            if row == len(matrix) -1:
                for num in matrix[row]:
                    if num == target:
                        return True
                return False
        