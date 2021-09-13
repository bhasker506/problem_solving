# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.

 

# Example 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

 

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 100
#     -104 <= matrix[i][j], target <= 104

from typing import List


class SearchItemInMatrix:
    
    def search_item(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False
        
        row_count = len(matrix)
        col_count = len(matrix[0])
        left = 0
        right = (row_count*col_count)-1
        
        while left <= right:
            mid = (left+right)//2
            mid_element = matrix[mid//col_count][mid%col_count]
            if target == mid_element:
                return True
            elif target < mid_element:
                right = mid-1
            else:
                left = mid+1
        return False
    
if __name__ == '__main__':
    obj = SearchItemInMatrix()
    print(obj.search_item([[1,1]], 3))