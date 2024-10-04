class Solution:
    def intToRoman(self, num: int) -> str:
        int_value=[1000, 9000, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]

        roman_value= ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_num = ""
        for i  in range(len(int_value)):
            while num >= int_value[i]:
                roman_num += roman_value [i]
                num -= int_value[i]
    return roman_num

# or
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return M[num // 1000] + C[num % 1000 // 100] + X[num % 100 // 10] + I[num % 10]