def remove_stars(s: str) -> str:
    stack = []
    for char in s:
        if char != "*":
            stack.append(char)
        else:
            stack.pop()
    return "".join(stack)


# Test Cases
print(remove_stars("ab**cd"))  # "cd"
print(remove_stars("abc*"))  # "ab"
