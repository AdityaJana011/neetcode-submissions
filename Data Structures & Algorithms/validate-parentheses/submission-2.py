class Solution:
    def isValid(self, s: str) -> bool:
        maping = {')':'(', '}':'{', ']':'['}

        stack = []

        for char in s:
            if char in maping:
                if not stack:
                    return False

                top = stack.pop()

                if top != maping[char]:
                    return False
            else: 
                stack.append(char)
        if stack:
            return False
        else:
            return True