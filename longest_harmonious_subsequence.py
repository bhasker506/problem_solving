from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        result = 0
        count = {}
        for i, v in enumerate(nums):
            count[v] = count.get(v) +1 if v in count else 1
        
        for key, value in count.items():
            if key+1 in count:
                result = max(result, value+count.get(key+1))
        return result
            
                
if __name__ == '__main__':
    s = Solution()
    # print(s.findLHS([1,3,2,2,5,2,3,7]))
    print(s.findLHS([1,1,1,1]))