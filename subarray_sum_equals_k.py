# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

from typing import List


class SubArraySumEqualsK:
    
    def sub_array_sum(self, nums: List, k: int) -> int:
        if not nums:
            return 0
        
        currsum = 0
        prevSum = dict()
        res = 0
        
        for i in range(len(nums)): 
            currsum += nums[i]
            if currsum == k: 
                res += 1
            
            if (currsum - k) in prevSum:
                res += prevSum[currsum - k]
        
            prevSum[currsum] = prevSum.get(currsum, 0)+1
        
        return res
            
            

if __name__ == '__main__':
    s = SubArraySumEqualsK()
    print(s.sub_array_sum(nums=[ 10, 2, -2, -20, 10 ], k=-10))
    # print(s.sub_array_sum(nums=[1,2,3], k=3))