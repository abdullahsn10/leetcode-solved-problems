from math import gcd


def gcd_of_strings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[: gcd(len(str1), len(str2))]


# Test cases
print(gcd_of_strings("abcabc", "abc"))  # abc
print(gcd_of_strings("abcabc", "abcabc"))  # abcabc\
print(gcd_of_strings("abcabc", "def"))  # ""
