from typing import List


class Solution(object):
    
    def segreagte(self, arr: List) -> List:
        if not arr:
            return None
        one_counter = 0
        loop_counter = 0
        
        while loop_counter < len(arr):
            if arr[loop_counter] == 1:
                arr[loop_counter] = 0
                arr[one_counter] = 1
                one_counter += 1
            loop_counter += 1
        return arr     


if __name__ == '__main__':
    obj = Solution()
    print(obj.segreagte(arr=[0,0,0,0,0,1]))