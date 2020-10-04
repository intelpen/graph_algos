class Solution:
    def myAtoi(self, input_string: str) -> int:
        state = "initial"
        number = 0
        sign = +1
        for character in input_string:
            #print(f"{state}:{character}:number={number}")
            if state == "initial":
                if character == " ":
                    continue
                elif character == "+":
                    sign = +1
                    state = "in_number"
                elif character == "-":
                    sign = -1
                    state = "in_number"
                elif character.isdigit():
                    state = "in_number"
                    number = int(character)
                else:
                    #expected +/-/digit/space
                    return 0
            elif state == "in_number":
                if character.isdigit():
                    number = number * 10 + int(character)
                else:
                    state = "end_number"
                    break
        int_min = -2 ** 31
        int_max = 2 ** 31 -1
        if number*sign> int_max:
            return int_max
        elif number*sign < int_min:
            return int_min
        else:
            return number*sign

if __name__ == "__main__":
    solution = Solution()
    tests = ["42", "     -42","4193 wtij wofds", "words and 987", "-91283472332"]
    for test in tests :
        print(f"{test} : {solution.myAtoi(test)}")