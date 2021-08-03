from typing import List
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        if not arr:
            return ""
        
        arr1 = sorted(arr, reverse=True)
        
        if arr1[len(arr)-1] > 2:
            return ""
        
        p = list(permutations(arr1))
        
        for h1,h2,m1,m2 in p:
            hours = h1*10+h2
            minute = m1*10+m2
            
            if hours < 24 and minute < 60:
                return f"{h1}{h2}:{m1}{m2}"
        return ""

if __name__ == '__main__':
    s = Solution()
    print(s.largestTimeFromDigits([1,2,3,4]))