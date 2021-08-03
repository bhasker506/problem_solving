class Solution:
    def decodeString(self, s: str) -> str:
        if not str:
            return str
        
        result = ""
        count = 0
        
        number_stack = []
        chars_stack = []
        
        while count < len(s):
            if s[count].isdigit():
                num = 0
                while(s[count].isdigit()):
                    num = (10 * num) + (ord(s[count]) - ord('0'))
                    count += 1
                number_stack.append(num)
            elif s[count] == '[':
                chars_stack.append(result)
                result = ""
                count += 1
            elif s[count] == ']':
                repeat_times = number_stack.pop()
                chars = chars_stack.pop()
                result = chars+ (repeat_times * result)
                count += 1
            else:
                result += s[count]
                count += 1
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.decodeString('b3[c]'))