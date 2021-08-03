class Numerals:
    def __init__(self, roman: str, value: int):
        self.roman = roman
        self.value = value

class Solution:
    def intToRoman(self, num: int) -> str:
        constants = [
            Numerals('M', 1000),
            Numerals('CM', 900),
            Numerals('D', 500),
            Numerals('CD', 400),
            Numerals('C', 100),
            Numerals('XC', 90),
            Numerals('L', 50),
            Numerals('XL', 40),
            Numerals('X', 10),
            Numerals('IX', 9),
            Numerals('V', 5),
            Numerals('IV', 4),
            Numerals('I', 1)
        ]
        
        result = ""
        for numeral in constants:
            div = num//numeral.value
            if div>0:
                result += numeral.roman * div
            num %= numeral.value
            
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1994))