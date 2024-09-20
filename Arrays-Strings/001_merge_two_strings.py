def merge(word1: str, word2: str) -> str:
    i, j = 0, 0
    size1, size2 = len(word1), len(word2)
    result = ""
    while i < size1 and j < size2:
        result += word1[i]
        result += word2[j]
        i += 1
        j += 1
    result += word1[i:]
    result += word2[j:]
    return result


# Test cases
print(merge("abc", "def"))  # adbecf
print(merge("abc", "defg"))  # adbecfg
