def reverse_words(s: str) -> str:
    words = []
    temp = ""
    for c in s:
        if c != " ":
            temp += c
        elif temp != "":
            words.append(temp)
            temp = ""
    if temp != "":
        words.append(temp)
    return " ".join(words[::-1])


# Test cases
print(reverse_words("the sky is blue"))  # "blue is sky the"
print(reverse_words("  hello world  "))  # "world hello"
print(reverse_words("a good   example"))  # "example good a"
