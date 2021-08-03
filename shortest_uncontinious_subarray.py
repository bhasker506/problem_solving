from typing import List


class Solution:
    
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums and len(nums) == 1:
            return 0
        
        mn = max(nums)
        mx = 0
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                mn = min(mn, nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                mx = max(mx, nums[i])
        
        left_index = 0
        right_index = len(nums)-1
        
        while left_index<len(nums):
            if mn<nums[left_index]:
                break
            left_index += 1
        
        
        while right_index >= 0:
            if mx>nums[right_index]:
                break
            right_index -= 1
        
        return right_index-left_index+1 if right_index-left_index>=0 else 0

    def findUnsortedSubarray1(self, N: List[int]) -> int:
        lenN, left, right = len(N) - 1, -1, -1
        maxN, minN = N[0], N[lenN]
        for i in range(1, len(N)):
            a, b = N[i], N[lenN-i]
            if a < maxN: right = i
            else: maxN = a
            if b > minN: left = i
            else: minN = b
        return max(0, left + right - lenN + 1)

if __name__ == '__main__':
    s = Solution()
    # print(s.findUnsortedSubarray1([1,2,3,5,4]))
    print(s.findUnsortedSubarray1([2,6,4,1,8,10,9,15]))
    # print(s.findUnsortedSubarray1([-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,-85,-84,-83,-82,-81,-80,-79,-78,-77,-76,-75,-65,-53,-73,-63,-67,-61,-39,-58,-56,-55,-68,-66,-74,-49,-60,-51,-62,-42,-47,-54,-43,-71,-64,-59,-45,-69,-57,-41,-70,-44,-46,-50,-48,-72,-52,-40,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]))