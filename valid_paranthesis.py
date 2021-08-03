# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Example 4:

# Input: s = "([)]"
# Output: false

# Example 5:

# Input: s = "{[]}"
# Output: true


class ValidParanthesis:
    
    def valid_parnthesis(self, s: str) -> bool:
        if not s:
            return False
        validator = {"(":")","[":"]","{":"}"}
        stack = []
        for c in s:
            if c in validator:
                stack.append(validator[c])
            else:
                if not stack:
                    return False
                top = stack[-1]
                if top != c:
                    return False
                stack.pop()
        return len(stack) == 0

if __name__ == '__main__':
    obj = ValidParanthesis()
    print(obj.valid_parnthesis("]"))  
