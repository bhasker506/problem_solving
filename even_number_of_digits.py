from typing import List


class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = 0
        for n in nums:
            even_count = 1
            while n > 9:
                n = n // 10
                even_count += 1
            if even_count % 2 == 0:
                result += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findNumbers(nums=[1, 345, 2, 6, 789]))