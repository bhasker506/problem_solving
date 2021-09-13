
class Atoi:
    
    def myAtoi(self, s: str) -> int:
        if not s:
            return s
        s = s.strip()
        is_negative = s[0] == '-'
        
        result = 0
        
        for c in s:
            if c == '.':
                break
            n = ord(c) - ord('0')
            if n in range(0, 10):
                result = (result*10)+n
        
        return max(-1* (2**31), -1*result) if is_negative else min((2**31)-1, result)

if __name__ == '__main__':
    obj= Atoi()
    obj.myAtoi("-91283472332")