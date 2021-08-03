from typing import List


class NextGreatestElement:
    
    def solution(self, arr: List) -> List:
        if not arr:
            return []
        stk = []
        for index, num in enumerate(arr):
            while stk and arr[stk[-1]] < num:
                arr[stk.pop()] = num
            stk.append(index)
        
        for index in stk:
            arr[index] = -1
        return arr

if __name__ == '__main__':
    s = NextGreatestElement()
    print(s.solution([5, 3, 2, 10, 12]))
