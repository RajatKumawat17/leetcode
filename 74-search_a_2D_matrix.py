class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # type: ignore
        nums_rows = len(matrix)
        nums_cols = len(matrix[0])

        for i in range(nums_rows):
            for j in range(nums_cols):
                if matrix[i][j] == target:
                    return True
        
        return False