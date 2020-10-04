"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
"""

class Solution:
    def intToRoman(self, number: int) -> str:
        # 1 to 3999
        ones = ["I","X","C","M"]
        fives =["V","L","D"]
        roman_str = ""
        digit_rang = 0
        while number:
            digit = number % 10
            print(f"{digit}:digit_rank:{digit_rang}")
            if digit <= 3:
                str_to_add = ones[digit_rang] * digit
            elif digit == 4:
                str_to_add = ones[digit_rang] + fives[digit_rang]
            elif digit <=8:
                str_to_add = fives[digit_rang] + ones[digit_rang] * (digit-5)
            elif digit ==9:
                str_to_add = ones[digit_rang] + ones[digit_rang+1]
            roman_str = str_to_add + roman_str
            number //= 10
            digit_rang += 1
        return roman_str
if __name__ == "__main__":
    solution = Solution()
    numbers = [3,4,9,58,1994]
    for number in numbers:
        print(f"{number} : {solution.intToRoman(number)}")
