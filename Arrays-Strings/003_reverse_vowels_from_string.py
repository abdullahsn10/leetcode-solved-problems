def reverse_vowels(s: str) -> str:
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1

    return "".join(s)


# Test cases
print(reverse_vowels("hello"))  # "holle"
print(reverse_vowels("leetcode"))  # "leotcede"
print(reverse_vowels("aA"))  # "Aa"
