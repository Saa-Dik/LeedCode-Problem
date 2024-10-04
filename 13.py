class Solution:
    def romanToInt(self, s: str) -> int:
        roman =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0
        num = 0
        for char in s[::-1]:
            value = roman[char]
            if value < num:
                val -= value
            else:
                val += value
            num = value
        return val 
                