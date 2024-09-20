def is_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    size_s, size_t = len(s), len(t)

    while i < size_s and j < size_t:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i != size_s:
        return False
    return True

# Test cases
print(is_subsequence("abc", "ahbgdc"))  # True
print(is_subsequence("axc", "ahbgdc"))  # False
print(is_subsequence("abc", "ahbgdc"))  # True

