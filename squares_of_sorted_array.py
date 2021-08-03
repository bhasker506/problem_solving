from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        left = 0
        right = len(nums) - 1
        result = [None] * len(nums)
        count = len(nums)-1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[count] = nums[left] * nums[left]
                left += 1
            else:
                result[count] = nums[right] * nums[right]
                right -= 1
            count -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedSquares(nums=[-4, -1, 0, 3, 10]))