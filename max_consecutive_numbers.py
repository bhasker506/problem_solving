from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return

        count = 0
        max_consecutive_count = 0
        while count < len(nums):
            if nums[count] == 0:
                count += 1
                continue
            consecutive_count = 0
            while count < len(nums) and nums[count] == 1:
                consecutive_count += 1
                count += 1
            max_consecutive_count = max(consecutive_count, max_consecutive_count)
        return max_consecutive_count

if __name__ == '__main__':
    sol = Solution()
    sol.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1])