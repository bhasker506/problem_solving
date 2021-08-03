from typing import List


class DegreeOfArray:
    
    def degree_of_array(self, nums: List):
        count_map = dict()
        first_seen = dict()
        degree = 0
        
        min_lenght = 0
        
        for index, val in enumerate(nums):
            if val not in first_seen:
                first_seen[val] = index
            
            count_map[val] = count_map.get(val, 0) + 1
            
            if count_map[val] > degree:
                degree = count_map[val]
                min_lenght = (index - first_seen[val]) + 1
            elif count_map[val] == degree:
                min_lenght = min(min_lenght, (index - first_seen[val]) + 1)
                
        return min_lenght

if __name__ == '__main__':
    d = DegreeOfArray()
    print(d.degree_of_array(nums=[2,1,1,2,1,3,3,3,1,3,1,3,2]))
        