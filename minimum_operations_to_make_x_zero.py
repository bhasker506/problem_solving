



import math
from typing import List


class MinimumOperationsForZero:
    
    def minOperations(self, nums: List[int], x: int) -> int:
        current = sum(nums)
        n = len(nums)
        mini = math.inf
        left = 0

        for right in range(n):
            # sum([0,..,left) + (right,...,n-1]) = x
            current -= nums[right]
            # if smaller, move `left` to left
            while current < x and left <= right:
                current += nums[left]
                left += 1
            # check if equal
            if current == x:
                mini = min(mini, (n-1-right)+left)

        return mini if mini != math.inf else -1

if __name__ == '__main__':
    obj = MinimumOperationsForZero()
    print(obj.minOperations([1,1,4,2,3], 5))