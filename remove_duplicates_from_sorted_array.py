

from typing import List


class RemoveDuplicates:
    
    def remove_duplicates(self, nums: List):
        if not nums:
            return
        
        index = 1
        
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1
        return nums[0:index]

if __name__ == '__main__':
    obj = RemoveDuplicates()
    nums = [0,1,1,2,2]
    print(obj.remove_duplicates([2,2]))