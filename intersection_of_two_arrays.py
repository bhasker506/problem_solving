# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


from typing import List


class Solution:
    
    def intersect(self, nums1: List, nums2: List) -> List:
        n1 = set(nums1)
        for n in nums2:
            n1.add(n)
        
        print(n1)


if __name__ == '__main__':
    s = Solution()
    s.intersect([1, 3, 2, 3, 4, 5, 5, 6], [3, 3, 5])
        
        
    