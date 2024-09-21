def is_valid(s: str) -> bool:
    stack = []
    mapping = {
        "{": "}",
        "(": ")",
        "[": "]",
    }
    # [( ]
    for c in s:
        if c in mapping:
            stack.append(c)
        else:
            if not len(stack):
                return False
            elif mapping[stack.pop()] != c:
                return False
    if len(stack) != 0:
        return False

    return True


# Test Cases
assert is_valid("()") == True
assert is_valid("()[]{}") == True
assert is_valid("(]") == False
assert is_valid("([)]") == False
