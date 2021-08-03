
class Solution:
    
    def happy_number(self, n: int) -> bool:
        if n == 1:
            return True
        
        all_sums = set()
        while n != 1:
            sum = 0
            current = n
            
            while current != 0:
                sum += (current%10) * (current%10)
                current //= 10
            
            if sum in all_sums:
                return False
            all_sums.add(sum)
            n = sum
        
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.happy_number(19))