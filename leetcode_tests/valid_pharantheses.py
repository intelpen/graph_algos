"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
class Solution:
    def sameParantheses(self, parantheses_str: str) -> bool:
        opened_parantheses = 0
        for character in parantheses_str:
            if character == "(":
                opened_parantheses +=1
            elif character == ")":
                opened_parantheses -=1
                if opened_parantheses<0:
                    return False
        return opened_parantheses==0
    def isValid(selfself, parantheses_str:str) -> bool:
        #use list or collections.deque or queue.LifoQueue
        oposed_dict = {")":"(","}":"{", "]":"["}
        parantheses_stack = []
        for character in parantheses_str:
            if character in oposed_dict:
                if (len(parantheses_stack)) == 0:
                    return False
                if oposed_dict[character] == parantheses_stack[-1]:
                    parantheses_stack.pop()
                else:
                    return False
            else:
                parantheses_stack.append(character)
        return len(parantheses_stack) == 0



if __name__ == "__main__":
    tests = [("()", True), (")", False)]
    solution = Solution()
    for parantheses_str, expected_result  in tests:
        obtained_result = solution.sameParantheses(parantheses_str)
        print(f"{parantheses_str}:expected:{expected_result}, obtained {obtained_result}")
    tests = [("()", True), ("()[]{}", True),("(]",False)]
    for parantheses_str, expected_result in tests:
        obtained_result = solution.isValid(parantheses_str)
        print(f"{parantheses_str}:expected:{expected_result}, obtained {obtained_result}")
