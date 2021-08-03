# 560. Subarray Sum Equals K
# Medium

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

 

# Constraints:

#     1 <= nums.length <= 2 * 104
#     -1000 <= nums[i] <= 1000
#     -107 <= k <= 107





from typing import List


class SublistWithSum:
    
    def subList_sum(self, nums:List, target: int) -> List:
        # create a dictionary for storing the end index of all sublists with
        # the sum of elements so far
        dict = {}
    
        # To handle the case when the sublist with the given sum starts
        # from the 0th index
        dict.setdefault(0, []).append(-1)
    
        sum_so_far = 0
        result = []
    
        # traverse the given list
        for index in range(len(nums)):
    
            # sum of elements so far
            sum_so_far += nums[index]
    
            # check if there exists at least one sublist with the given sum
            if (sum_so_far - target) in dict:
                print(*[nums[value+1: index+1] for value in dict.get(sum_so_far-target)], end=' ')
    
            # insert (sum so far, current index) pair into the dictionary
            dict.setdefault(sum_so_far, []).append(index)
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}
        sum = 0
        result = 0
        for num in nums:
            sum += num
            if sum - k in sum_dict:
                result += sum_dict[sum - k]
            sum_dict[sum] = sum_dict.get(sum, 0)+1
        return result

if __name__ == '__main__':
    obj = SublistWithSum()
    obj.subList_sum([3, 4, -7, 1, 3, 3, 1, -4], 7)
    print(obj.subarraySum([3, 4, -7, 1, 3, 3, 1, -4], 7))