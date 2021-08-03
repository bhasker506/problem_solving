# 415. Add Strings
# Easy

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"

 

# Constraints:

#     1 <= num1.length, num2.length <= 104
#     num1 and num2 consist of only digits.
#     num1 and num2 don't have any leading zeros except for the zero itself.

class AddStrings:
    
    def add_strings(self, num1: str, num2: str):
        if not num1 and not num2:
            return num1
        
        carry = 0
        num1_lenght = len(num1)-1
        num2_lenght = len(num2)-1
        
        result = ''
        
        while num1_lenght >= 0 or num2_lenght >=0:
            s = 0
            s += carry
            if num1_lenght >= 0:
                s += ord(num1[num1_lenght]) - ord('0')
            if num2_lenght >= 0:
                s += ord(num2[num2_lenght]) - ord('0')
            num1_lenght -= 1
            num2_lenght -= 1
            
            if s >=10:
                carry = 1
                result += f'{s%10}'
            else:
                carry = 0
                result += str(s)
        
        if carry > 0:
            result += str(carry)
        return result[::-1]

if __name__ == '__main__':
    obj = AddStrings()
    print(obj.add_strings(num1='456', num2='77'))
    