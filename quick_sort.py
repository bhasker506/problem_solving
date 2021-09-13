


from typing import List


class QuickSort:
    
    def quick_sort(self, nums:List, start, end) -> List:
        if (start < end):
         
            # p is partitioning index, array[p]
            # is at right place
            p = self.partition(start, end, nums)
            
            # Sort elements before partition
            # and after partition
            self.quick_sort(nums, start, p - 1)
            self.quick_sort(nums, p + 1, end)
    
    def partition(self, low: int, high: int, nums: List) -> int:
        pivot_index = low
        pivot = nums[low]
        
        while low < high:
            while low < len(nums) and nums[low] <= pivot:
                low += 1
            
            while high>=0 and nums[high] > pivot:
                high -= 1

            if low<high:
                nums[low], nums[high] = nums[high], nums[low]
        nums[high], nums[pivot_index] = nums[pivot_index], nums[high]
        return high


if __name__ == '__main__':
    obj = QuickSort()
    nums = [50,30,10]
    obj.quick_sort(nums, 0, len(nums)-1)
    print(nums)