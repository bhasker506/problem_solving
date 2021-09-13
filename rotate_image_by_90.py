# 48. Rotate Image
# Medium

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Example 3:

# Input: matrix = [[1]]
# Output: [[1]]

# Example 4:

# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]


from typing import List


class  RotateImage:
    
    
    def rotate_image(self, matrix: List[List[int]]):
        if not matrix or not len(matrix[0]):
            return
        
        row_count = len(matrix)
        col_count = len(matrix[0])
        
        for row in range(row_count):
            for col in range(row, col_count):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
    
        for row in range(row_count):
            matrix[row] = matrix[row][::-1]
        
        return matrix

if __name__ == '__main__':
    obj = RotateImage()
    print(obj.rotate_image([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))