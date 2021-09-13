# 75. Sort Colors
# Medium

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

# Example 3:

# Input: nums = [0]
# Output: [0]

# Example 4:

# Input: nums = [1]
# Output: [1]

 

# Constraints:

#     n == nums.length
#     1 <= n <= 300
#     nums[i] is 0, 1, or 2.


from typing import List


class SortColors:
    
    def sort_colors(self, nums: List) -> None:
        if not nums or len(nums)==1:
            return
        
        start = 0
        end = len(nums)-1
        index = start
        
        while index <= end:
            if nums[index] == 0:
                nums[index], nums[start] =  nums[start], nums[index]
                index += 1
                start += 1
            elif nums[index] == 2:
                nums[index], nums[end] =  nums[end], nums[index]
                end -= 1
            else:
                index += 1


if __name__ == '__main__':
    obj = SortColors()
    nums = [0,1,2,0,1,2,0,1,2]
    obj.sort_colors(nums)
    print(nums)