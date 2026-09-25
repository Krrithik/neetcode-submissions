class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: 
            return False

        brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []

        for i in s:
            if len(stack) == 0:
                if i in brackets:
                    return False

            if i in brackets.values():
                stack.append(i)
            elif brackets[i] == stack[-1]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


        