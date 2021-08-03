from typing import List


class Solution:
    
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        a, b = 0,1
        if not nums:
            if lower == upper:
                return [f"{lower}"]
            else:
                return [f"{lower}->{upper}"]
        
        result = []
        
        if nums[0] > lower:
            result.append(f"{lower}->{nums[0]-1}")    
            
        while b < len(nums):
            if nums[b] != nums[a]+1:
                if nums[a]+1 == nums[b]-1:
                    result.append(f"{nums[a]+1}")
                else:
                   result.append(f"{nums[a]+1}->{nums[b]-1}") 
            a += 1
            b += 1
            
        if nums[-1]<upper:
            result.append(f"{nums[-1]+1}->{upper}")  
            
        return result

if __name__ == '__main__':
    s = Solution()
    res = s.findMissingRanges(nums=[-1], lower=-2, upper=-1)
    print(res)